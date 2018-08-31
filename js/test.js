$(function() {
$('#btn-test').click(function() {//(function( event ) {
  var seconds = 30; 
  if($('#progress-test').hasClass('visible')) // если кликнули по кнопке остановить - сбросить все
  {
    clearInterval(int);
    $('#seconds').text(seconds);
    $('#progress-bar-test').css('width',"0%");
    $('#btn-test').html('Тест');
    $('#progress-test').removeClass('visible')
    if($('#rand-result').hasClass('visible')) 
    {
      $('#rand-result').removeClass('visible');
    }
    
  }
  else // если кликнули по кнопке тест
  {
    $('#btn-test').html('Остановить');
    $('#progress-test').addClass('visible');
    var timetotal = $('#seconds').text();
    int = setInterval(function() { 
      if (timetotal > 0) {
        timetotal--;
        $('#seconds').text(timetotal);
        var progress = ((seconds - timetotal)/seconds)*100;
        $('#progress-bar-test').css('width', progress+'%'); 
      } 
      else {
        clearInterval(int);
        var arr = []; // закончился временной интервал - ищем рандомное значение
        for(i=1002; i<1011; i+=1)
        {
          if ((i!=1007)&&(i!=1009))
          {
            arr.push(i)
          }
        }
        var rand = Math.floor(Math.random() * arr.length);
        $('#rand-result').addClass('visible');
        $('#impuls').text(arr[rand]);
      }
    }, 1000);
  }
  return false;
});
});
