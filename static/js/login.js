document.getElementById('toggle_password').onclick = function(e) {
    const isPass = this.previousElementSibling.type === 'password'
    this.previousElementSibling.type = isPass ? 'text' : 'password'
    $(this).children('i').toggleClass('bi-eye-slash bi-eye')
}