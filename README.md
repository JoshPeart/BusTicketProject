# BusTicketProject
<ul>A user interface to the NCTX bus tickets</ul>


<h1>Use Case 1 - Application Start and User Authentication</h1>
<p>The user will be welcomed to the app, prompted to log in, or continue as a guest.</p>
<ul>Displays a welcome screen with login options</ul>
<ul>User can:
  <ul>Log in with a username and password</ul>
  <ul>Continue as a guest</ul>
</ul>
<ul>These logged in users will be assigned with a role (<i>Admin</i> or <i>Customer</i>)</ul>
<ul>Guest users can browse tickets but not complete purchases, they will be prompted to log in</ul>


<h1>Use Case 2 - Main Menu Display, General Introduction</h1>
<ul>display the main menu instructions
  <ul>Ask user to enter option number</ul>
  <ul>Validate number is within the range of options</ul>
  <ul>Read file (mobile_products.csv)</ul>
  <ul>filter tickets belonging to that category</ul>
  <ul>Display the results to the user</ul>
</ul>


<h1>Use Case 3 - Ticket purchase process</h1>
<p>Allow the logged in users to be able to purchase tickets</p>
<ul>Show all of the available tickets within the selected category</ul>
<ul>User selects a ticket using its code</ul>
<ul>Program displays:
  <ul>Ticket title</ul>
  <ul>Price in pounds</ul>
</ul>
<ul>If the user is a guest:
  <ul>They are prompted to log in</ul>
  <ul>Purchase is cancelled if login fails</ul>
</ul>
<ul>User confirms or cancels the purchase</ul>


<h1>Use Case 4 - Transaction Recording</h1>
<p>Saving successful purchases</p>
<ul>On confirmation, the transaction will be marked as successful</ul>
<ul>Created a new csv file that will be appended to (purchases.csv)
  <ul>Saving ticket code, title and the price paid</ul>
</ul>


<h1>Use Case 5 - Program Continuation or Exit</h1>
<p>Making the app more user friendly</p>
<ul>User is asked wether they want to return to the main menu</ul>
<ul>If yes:
  <ul>Program restarts from the main menu screen</ul>
</ul>
<ul>If no:
  <ul>Program exits with a goodbye message</ul>
</ul>

