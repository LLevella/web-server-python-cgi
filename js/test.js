$(function() {
  var timer;
  $('#btn-test').click(function() {//(function( event ) {
    var seconds = 30; 
    var beginr = 1002;
    var endr = 1010;
    var ex1 = 1007;
    var ex2 = 1009;
    $('#seconds').text(seconds);
    if($('#rand-result').hasClass('visible')) 
    {
      $('#rand-result').removeClass('visible');
    }

    if($('#btn-test').html() == 'Остановить') // если кликнули по кнопке остановить - сбросить все
    {
      clearInterval(timer);
      $('#progress-bar-test').css('width',"0%");
      $('#btn-test').html('Тест');
      $('#progress-test').removeClass('visible')
    }
    else // если кликнули по кнопке тест
    {
      $('#btn-test').html('Остановить');
      $('#progress-test').addClass('visible');
      var timetotal = seconds;
      
      timer = setInterval(function() { 
        if (timetotal > 0) {
          timetotal--;
          $('#seconds').text(timetotal);
          var progress = ((seconds - timetotal)/seconds)*100;
          $('#progress-bar-test').css('width', progress+'%'); 
        } 
        else {
          clearInterval(timer);
          var rand = 0;
          do {
            rand = beginr + Math.random() * (endr + 1 - beginr);
            rand = Math.floor(rand);
          } while ((rand == ex1)&&(rand == ex2));
          $('#rand-result').addClass('visible');
          $('#impuls').text(rand);
          $('#btn-test').html('Тест');
          $('#progress-test').removeClass('visible')
          $('#progress-bar-test').css('width',"0%");
        }
      }, 1000);
    }
  });
  });