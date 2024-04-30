from flask import Flask,request,redirect

import stripe

app = Flask(__name__, static_url_path="", static_folder="public")

stripe.api_key = "sk_test_51PA35NP5aaTST0VYmc1HXAJ66ACY82PmmzyW4chbupQORCADq5dalNVjn4VXSHt9W8slCvz1tlXT5na5a6gPqOcn00kVGE45gH"

YOUR_DOMAIN = "https://serpentstrikes3bucket.s3.ap-southeast-2.amazonaws.com"

@app.route('/create-checkout-session1', methods=['POST'])
def create_checkout_session1():
    try:
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1PAkyEP5aaTST0VYr6YuFgWK',
                    'quantity':1 
                }
            ], 
            mode="payment",
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url= YOUR_DOMAIN + "/cancel.html"
        )
        
    
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url,code=303)
@app.route('/create-checkout-session2', methods=['POST'])
def create_checkout_session2():
    try:
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1PAsOEP5aaTST0VYuh9iiYzS',
                    'quantity':1 
                }
            ], 
            mode="payment",
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url= YOUR_DOMAIN + "/cancel.html"
        )
        
    
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url,code=303)
@app.route('/create-checkout-session3', methods=['POST'])
def create_checkout_session3():
    try:
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1PAsOyP5aaTST0VYDxpCWVc9',
                    'quantity':1 
                }
            ], 
            mode="payment",
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url= YOUR_DOMAIN + "/cancel.html"
        )
        
    
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url,code=303)
@app.route('/create-checkout-session4', methods=['POST'])
def create_checkout_session4():
    try:
        
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1PAsPTP5aaTST0VYhc0KCLsg',
                    'quantity':1 
                }
            ], 
            mode="payment",
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url= YOUR_DOMAIN + "/cancel.html"
        )
        
    
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url,code=303)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
