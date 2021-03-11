$.get( "https://fa-python-backend.herokuapp.com/api/fa", function( data ) {
  console.log(data)
  $( ".result" ).html( data );
  alert( "Load was performed." );
});
