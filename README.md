First, this project can complete the basic functions, like create an account, login, logout, handle login failure. The link for log in is http://vcm-xxxxx.vm.duke.edu:8000/login. And you can fullfill the jump between several broswers.

After you have logged in, You will be in our home page, also known as 'choose role' page, since this project can be divided as three parts, one for ride request owner, one for driver, one for sharer. And you can see three url link which will guild you to the specific role.

For role ride request owner, you can see have the links for 
'home' : it's the home page for ride request owner,
'new ride request' : page for submit a new ride request, 
'own'  : page for find all ride requests that you(the user) be the owner(user can see other requests when they are a driver or a sharer in the other two part)
'own-confirmed' : page for find all confirmed ride requests that the user belong
'own-uncomplete' : page for find all uncoompleted ride requests that the user belong
Also, in those pages there are links for user to update their ride request, or see the detail of their ride request.

For role driver, the pages are:
‘home’: page for driver
‘search’: view all the open rides for you as a driver, filtered by capacity (should be greater than sum = number of the owner party + number of the sharer party), optional vehicle type. You can directly confirm a ride from this page
‘view detail’: Once you confirm a ride, the page goes to all the rides you have. Then you can view the whole list and click on each ride request title (id) to view detailed information.
‘edit status’: You can complete one ride both on that specific ride detail page and your confirmed ride list. Once you complete, this ride is no longer open, it shows “is complete” and there’s no complete button any more.
‘register driver’: 1. You can click on “register or update vehicle”, if you are not registered as a driver, you would be redirect to register as a driver. After submitting, profile of this user updates to is_driver = True, binding his vehicle and pops up a success alert to tell you “Registration Succeed”; 2. If you choose the role to be a driver or click on driver’s homepage when not registered as a driver, it will tell you that “You haven't registered as a driver!” And has a link for you to register. 3. If you type /drive/create/ after you have already been a driver, it would alert you that you have already registered your vehicle and redirect to the update vehicle page.
‘update vehicle’: you register one vehicle when you first register as a driver. If you click on “register or update vehicle” after you already are a driver, it pops up an update form and you could make changes.

“User authenticate”: If you are trying to complete an unconfirmed ride via URL, you would be redirected to search page with a warning:"You can't complete an unconfirmed ride!Please see open rides for you!" ; If you are trying to complete a confirmed ride which doesn't belongs to you, you would be redirected to your own confirmed list with a warning:"Permission denied: Only driver of this ride can complete this request!"

For role sharer, the pages are:
'home' : page for share
'search': find all open ride requests
After you find the request you want, there are two links for each request, onefor watch them in detail, one for apply as a sharer of the reuqest, and when you apply to be a sharer, you can also type a few attributes of ride request.



Also, for better-looking, I used the .css setting which recommanded by a YouTube programmer. The github link of his repository is here:
 https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHMyUlotMEZZenhYQV9rSzZEdVVnblhPd01qUXxBQ3Jtc0tuYlVSZnFjTWU2eGZnNEZwbUpSb1NXbXJVVTN1RjcwV0oxTkxaaUdZT1AwcW91UVJtZXBjMGJSMmZ3UGc3Z0I5V2RHUk52Mm1MZU14SExKa2dxalpQTE5mRnpBc0FUV3NRWmNEOG5yNTZPUmRvVHdRTQ&q=https%3A%2F%2Fgithub.com%2FCoreyMSchafer%2Fcode_snippets%2Ftree%2Fmaster%2FDjango_Blog
