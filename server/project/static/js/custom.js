document.addEventListener('DOMContentLoaded', function () {
  var phoneInput = document.getElementById('id_phone_number');
  var maskOptions = {
    mask: '+{7}(000)-000-00-00'
  };
  var mask = IMask(phoneInput, maskOptions);
});


// $(document).ready(function() {
//   $('#submit-btn').click(function(e) {
//     e.preventDefault(); // prevent the default action
//     $.ajax({
//       url: '/',
//       type: 'POST',
//       headers: {
//         'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()
//       },
//       data: $('#form').serialize(),
//       success: function(response) {
//         if (response.success) {
//           $('#exampleModal').modal('show');
//           $('#form')[0].reset();
//         } else {
//           // Handle errors here
//         }
//       }
//     });
//   });
// });

