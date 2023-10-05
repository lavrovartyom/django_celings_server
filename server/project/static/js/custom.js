$(document).ready(function() {
  $('#phone').inputmask("+7(999)-999-99-99");
});

$(document).ready(function() {
  $('#submit-btn').click(function(e) {
    e.preventDefault(); // prevent the default action
    $.ajax({
      url: '/',
      type: 'POST',
      headers: {
        'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()
      },
      data: $('#form').serialize(),
      success: function(response) {
        if (response.success) {
          $('#exampleModal').modal('show');
          $('#form')[0].reset();
        } else {
          // Handle errors here
        }
      }
    });
  });
});

