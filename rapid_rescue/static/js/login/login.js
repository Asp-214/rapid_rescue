$(document).ready(function(){
    $('#login-in').submit(function(e){
        e.preventDefault();
        var formData = $(this).serialize();
        var Incorrect = document.getElementById('incorrect');
        var notexist = document.getElementById('notexist');
        var spinner = document.getElementById('loading-bar-spinner')
        spinner.style.display = 'block'
        $.ajax({
            type: 'POST',
            url: 'auth/verify/',
            data: formData,
            success: function(response){
                switch (response.status) {
                    case 0:
                        window.location.href = "/dashboard"
                        break;

                    case 1:
                        Incorrect.classList.add('block-display');
                        notexist.classList.remove('block-display');
                        break;

                    case -1:
                        notexist.classList.add('block-display');
                        Incorrect.classList.remove('block-display');
                        break;
                }
                spinner.style.display = 'none'
            }
        });
    });
});
