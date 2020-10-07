# Simple-KB

This knowledge base models the main interactive components of an online webstore
ie: creating an account, placing an order, viewing order history etc. 
These rules were established by taking into consideration how an automated system/robot 
would navigate a website in place of a human to interact with the different components. 

Usage Examples:

EXAMPLE 1: Simple Account Login
Telling email & password will infer that the user has logged into his/her account
--------------------------------------------------------------------------------------
load a4_q2_kb.txt
tell email password
infer_all

EXAMPLE 2: Simple Account Subscription
Telling a new_email and new_password will infer the user has agreed to subscribe to the 
store. His/her email will be inferred for future uses on the website such as later on
in the checkout page where the account holder's email is required under contact info
--------------------------------------------------------------------------------------
load a4_q2_kb.txt
tell new_email new_password
infer_all

EXAMPLE 3: Place an Order
These series of calls to tell and infer_all steps through the different stages of placing
an order on a webstore from choosing items to viewing the cart, viewing the checkout page
and finally placing the order.
--------------------------------------------------------------------------------------
load a4_q2_kb.txt
tell correct_url items_chosen view_cart_button
infer_all
tell checkout_button
infer_all
tell first_name last_name email house_number street postal_code
infer_all
tell place_order_button
infer_all




