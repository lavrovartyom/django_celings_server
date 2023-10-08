$(document).ready(function() {
  $('#phone').inputmask("+7(999)-999-99-99");
});

$(document).ready(function() {
  $('#submit-btn').click(function() {
    $.ajax({
//      url: '{% url "home" %}',
      url: '/',
      type: 'POST',
      data: $('#form').serialize(),
      success: function(response) {
        if (response.success) {
          $('#exampleModal').modal('show');
          $('#form')[0].reset();
        }
      }
    });
  });
});
