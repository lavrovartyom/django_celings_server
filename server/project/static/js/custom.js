// Маска номера телефона в форме заявки
document.addEventListener('DOMContentLoaded', function () {
  var phoneInput = document.getElementById('id_phone_number');
  var maskOptions = {
    mask: '+{7}(000)-000-00-00'
  };
  var mask = IMask(phoneInput, maskOptions);
});


// Функция для валидации формы заявки
document.addEventListener('DOMContentLoaded', function () {
    var submitBtn = document.getElementById('submit-id-submit');
    var form = document.getElementById('form');

    submitBtn.addEventListener('click', function (e) {
        e.preventDefault();

        var xhr = new XMLHttpRequest();
        var formData = new FormData(form);

        xhr.open('POST', '/');
        xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.success) {
                    new bootstrap.Modal(document.getElementById('successModal')).show();
                    form.reset();
                } else {
                    // Обработка ошибок
                    form.reportValidity(); // Это для вызова стандартной валидации
                }
            }
        };

        xhr.send(formData);
    });
});



