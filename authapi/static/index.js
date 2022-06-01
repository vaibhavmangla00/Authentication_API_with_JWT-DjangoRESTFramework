const register = document.querySelector('.register')
const login = document.querySelector('.login')
const changePassword = document.querySelector('.change-password')
const forgotPassword = document.querySelector('.resetpassword')

register.onclick= () =>{
    document.querySelector(".register-form").classList.remove('hide')
}

login.onclick= () =>{
    document.querySelector(".login-form").classList.remove('hide')
}

changePassword.onclick= () =>{
    document.querySelector(".change-password-form").classList.remove('hide')
}

forgotPassword.onclick= () =>{
    document.querySelector(".resetpassword-form").classList.remove('hide')
}
