from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

class ShoppingListApplication():
    def __init__(self, name):
        self.name = name
        self.users = []
        self.shopping_lists = []
        self.shopping_list = {}
        self.content = {}
        self.category = ''
        self.items = []
        self.registered = ['f@gmail.com', 'g@gmail.com']
        self.passwords = ['small', 'tiny', 'little']

    # Method to get individual shopping list items as a list
    def get_items(self, item_name):
        my_items = ['speaker |', ' DVD player |', ' Television set |', ' Laptop |', ' Sound system']

        for i in my_items:
            self.items.append(i)  # Append each item to a list
        cat = 'Electronics'  # Get category name possibly from dropdown menu
        self.get_category(cat)

    # Get category name and prepare for content creation
    def get_category(self, list_category):
        self.category = list_category
        self.create_content(list_category, self.items)

    # Create the content. Returns a dictionary k = category_name, v = items_in_list
    def create_content(self, category, items):
        self.content[category] = items
        name = "December wish"  # Get form input, Let user suggest
        self.get_shopping_list(name, self.content)

    # Prepare shopping list. Returns a dictionary
    def get_shopping_list(self, list_name, content):
        self.shopping_list[list_name] = content
        self.get_shopping_lists(list_name)

    # Prepare shopping lists. A person can have many shopping lists so store in a list -> for now
    def get_shopping_lists(self, name):
        self.shopping_lists.append(name)

    # Package all data into objects of the class Users
    def packager(self):
        self.get_items('name')  # Call get items since we need it call other methods that are part of the chain
        obj2 = Users('john', self.shopping_list)
        self.users.append(obj2.store())
        obj2 = Users('mary', self.shopping_list)
        self.name = obj2.username
        self.users.append(obj2.store())
        obj2 = Users('mary', self.shopping_list)
        self.name = obj2.username
        self.users.append(obj2.store())
        obj2 = Users('mary', self.shopping_list)
        self.name = obj2.username
        self.users.append(obj2.store())
        obj2 = Users('mary', self.shopping_list)
        self.name = obj2.username
        self.users.append(obj2.store())
        obj2 = Users('Timothy J', self.shopping_list)
        self.name = obj2.username
        self.users.append(obj2.store())


class Users:
    def __init__(self, username, listname):
        self.username = username
        self.listname = listname

    def store(self):
        user = [self.username, self.listname]
        print(user)
        return user


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    obj = ShoppingListApplication('n')
    obj.packager()
    for i in range(len(obj.users)):
        whole = obj.users[i]
        print(whole)
    for j in range(len(whole)):
        user_name = whole[j]
        obj.username = user_name
        print(obj.username)
    s_dict = whole[1]
    for k in s_dict:
        s_list_name = k
    obj.shopping_list_name = s_list_name
    print(obj.shopping_list_name)
    temp = s_dict[s_list_name]
    # print(temp)
    for key in temp:
        category = key
    obj.category = category
    print(obj.category)
    shopping_list_items = temp[category]
    obj.items = shopping_list_items
    print(obj.items)
    str1 = ''.join(obj.items)
    return render_template("dashboard.html", users=obj.users, d_name=obj.name, d_cat=obj.category,
                           ulist=obj.shopping_list_name, d_items=str1)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def validd():
    email = ''
    password = ''
    cred = False
    obj = ShoppingListApplication('n')
    registered = obj.registered
    passwords = obj.passwords
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    if email is None:
        cred = False
    elif password is None:
        cred = False
    if email in registered:
        if password in passwords:
            cred = True
            return render_template("dashboard.html", cred=cred)
        else:
            cred = False
            return render_template("signup.html", cred=cred)
    else:
        return render_template("signup.html", cred=cred)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


