document.addEventListener('DOMContentLoaded', function () {
  var phoneInput = document.getElementById('id_phone_number');
  var maskOptions = {
    mask: '+{7}(000)-000-00-00'
  };
  var mask = IMask(phoneInput, maskOptions);
});


document.addEventListener('DOMContentLoaded', function () {
    var submitBtn = document.getElementById('submit-id-submit');

    submitBtn.addEventListener('click', function (e) {
        e.preventDefault();

        var xhr = new XMLHttpRequest();
        var formData = new FormData(document.getElementById('form'));

        xhr.open('POST', '/');
        xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if (response.success) {
                    new bootstrap.Modal(document.getElementById('successModal')).show();
                    document.getElementById('form').reset();
                } else {
                    // Обработка ошибок
                }
            }
        };

        xhr.send(formData);
    });
});


