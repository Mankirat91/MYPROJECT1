function login(email,password){
   var emailExist=getUserByEmail(email)
    var messages=getMessages();
   if(!emailExist) return messageHandler(messages.EMAIL_INCORRECT,'error')
   var passwordExist=getUserByPassword(password)
   if(!passwordExist) return messageHandler(messages.PASSWORD_INCORRECT,'error')
   setLocalData('userId',passwordExist.id);
   routeTo('/');
}

function submitForm(){
   var form= document.querySelector('#login-form');
   form.addEventListener('submit',(e)=>{
     e.preventDefault();
     var email=  document.getElementById('email').value;
     var password=  document.getElementById('password').value;
     login(email,password)
   })
}
function checkIfLogin(){
  var check=getLocalData('userId') ? JSON.parse(getLocalData('userId')) : '';
  if(check) {
     var loginPage= document.getElementById('login-page');
     var p= document.createElement('p');
     p.innerHTML=`You have already login you can logout <a href="javascript.void(0)" onclick="logout()" id="logout"> here</a>`;
     loginPage.innerHTML=p.outerHTML;
  }
  else{
    getLoginForm();
    submitForm();
  }
}

function logout(){
    window.event.preventDefault();
    setLocalData('userId',"");
    routeTo('/');
}

function getLoginUser(){
    var userId=getLocalData('userId') ? JSON.parse(getLocalData('userId')) : '';
    return userId;
}

function getLoginForm(){
    var loginPage= document.getElementById('login-page');
    var form= document.createElement('form');
    var email= document.createElement('input');
    var password= document.createElement('input');
    var button= document.createElement('button');
    var messages= document.createElement('div');
    form.id="login-form";
  
    email.id="email";
    email.className="w-100 form-control border-0 py-3 mb-4";
    email.setAttribute('placeholder',"Enter Your Email")
    email.setAttribute('type',"email")
    email.setAttribute('required',true)

    password.id="password";
    password.className="w-100 form-control border-0 py-3 mb-4";
    password.setAttribute('placeholder',"Enter Your Password")
    password.setAttribute('type',"password")
    password.setAttribute('required',true)

    button.className="w-100 btn form-control border-secondary py-3 bg-white text-primary"
    button.setAttribute('type',"submit")
    button.innerText="login"

    messages.id="messages";
    form.append(email)
    form.append(password)
    form.append(button)
    form.append(messages)
    loginPage.innerHTML=form.outerHTML;   
}