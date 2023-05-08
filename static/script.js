// This function submits the form data to the Flask app using AJAX and displays the translation
function translate() {
    // Get the form data
    var formData = {
      'from_lang': $('#from_lang').val(),
      'to_lang': $('#to_lang').val(),
      'text': $('#text').val()
    };
  
    // Send the AJAX request
    $.ajax({
      type: 'POST',
      url: '/',
      data: formData,
      dataType: 'json',
      encode: true
    })
  
    // Display the translation on the page
    .done(function(data) {
      var translation = data.translation;
      $('.translation').html('<h2>Translation:</h2><p>' + translation + '</p>');
    })
  
    // Display an error message if the translation failed
    .fail(function() {
      $('.translation').html('<p>Translation failed.</p>');
    });
  }
  
  // Attach the translate() function to the form submit event
  $('form').submit(function(event) {
    event.preventDefault(); // Prevent the default form submit behavior
    translate(); // Call the translate() function
  });
  