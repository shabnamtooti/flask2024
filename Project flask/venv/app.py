from flask import Flask,render_template,request,url_for,session,redirect
app=Flask(__name__)
app.secret_key='your_secret_key'
app.config['SESSION_TYPE']='filesystem'
#داده های نمومه برای فروشگاه
products=[
    {'name':'Dog Food','price':30,'image':'images/products1.jpg','Description':'These foods are dry and for small dogs'},
    {'name':'Cat Food','price':40,'image':'images/products2.jpg','Description':'These foods are dry and suitable for adult cats'},
    {'name':'Toys','price':50,'image':'images/products3.jpg','Description':'These toys are dental and are designed to clean teeth'},
    {'name':'Maintenance Supplies','price':65,'image':'images/products4.jpg','Description':'Includes boxes and collars... Is'},
    {'name':'Health','price':67,'image':'images/products5.jpg','Description':'Shampoos,conditioners,toothpastes and medicines'}
]
comments=[]
ratings=[]
users=[]
@app.route('/products',methods=['GET'])
def products_view():
    return render_template('products.html',products=products)
@app.route('/',methods=['GET'])
def index():
    search_query=request.args.get('query','')
    filtered_product=[p for p in products if search_query.lower()in p['name'].lower()]
    return render_template('index.html',products=filtered_product,comments=comments)
@app.route('/search',methods=['GET'])
def search():
    query=request.args.get('query') #گرفتن مقدار جستجو شده
    filtered_products=[p for p in products if query.lower()in p['name'].lower()]
    return render_template('search_results.html',query=query,products=filtered_products)
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart']=[]
    session['cart'].append(product_id)
    return redirect(url_for('index'))
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username not in users:
            users[username]=password
            return redirect(url_for("login"))
        return render_template('register.html')
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username in users and users[username]==password:
            session['username']=username
            return redirect(url_for("index"))
        return render_template("ligin.html")
@app.route('/add_comment',methods=['POST'])
def add_comment():
    comment_text=request.form['comment']
    comments.append(comment_text)
    return redirect(url_for('index'))
@app.route('/rate',methods=["POST"])
def rate():
    rating=request.form['rating']
    rating.append(int(rating))
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)