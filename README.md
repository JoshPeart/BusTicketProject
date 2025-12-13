# BusTicketProject
<ul>A user interface to the NCTX bus tickets</ul>


<h1>Use Case 1 - Application Start and User Authentication</h1>
<p>The user will be welcomed to the app, prompted to log in, or continue as a guest.</p>

<ul>
  <li>Displays a welcome screen with login options</li>
  <li>User can:
    <ul>
      <li>Log in with a username and password</li>
      <li>Continue as a guest</li>
    </ul>
  </li>
  <li>These logged in users will be assigned with a role (<i>Admin</i> or <i>Customer</i>)</li>
  <li>Guest users can browse tickets but not complete purchases, they will be prompted to log in</li>
</ul>

<h1>Use Case 2 – Main Menu Display, General Introduction</h1>
<ul>
  <li>Displays the main menu instructions</li>
  <li>Ask user to enter option number</li>
  <li>Validate number is within the range of options</li>
  <li>Read file (<code>mobile_products.csv</code>)</li>
  <li>Filter tickets belonging to that category</li>
  <li>Display the results to the user</li>
</ul>

<h1>Use Case 3 – Ticket Purchase Process</h1>
<p>Allow logged-in users to purchase tickets.</p>

<ul>
  <li>Show all available tickets within the selected category</li>
  <li>User selects a ticket using its code</li>
  <li>Program displays:
    <ul>
      <li>Ticket title</li>
      <li>Price in pounds (£)</li>
    </ul>
  </li>
  <li>If the user is a guest:
    <ul>
      <li>They are prompted to log in</li>
      <li>Purchase is cancelled if login fails</li>
    </ul>
  </li>
  <li>User confirms or cancels the purchase</li>
</ul>

<h1>Use Case 4 – Transaction Recording</h1>
<p>Saving successful purchases.</p>

<ul>
  <li>On confirmation, the transaction is marked as successful</li>
  <li>Purchase details are saved to <code>purchases.csv</code>:
    <ul>
      <li>Ticket code</li>
      <li>Ticket title</li>
      <li>Price paid</li>
    </ul>
  </li>
</ul>

<h1>Use Case 5 – Program Continuation or Exit</h1>
<p>Making the app more user friendly.</p>

<ul>
  <li>User is asked whether they want to return to the main menu</li>
  <li>If yes:
    <ul>
      <li>Program restarts from the main menu</li>
    </ul>
  </li>
  <li>If no:
    <ul>
      <li>Program exits with a goodbye message</li>
    </ul>
  </li>
</ul>

