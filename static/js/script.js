/*jshint esversion: 6 */
/*Adapted fron https://codepen.io/bengoddard*/

function openToday (){
    var currentDate = new Date();
    var weekday = [];
    weekday[0] = "Sunday";
    weekday[1] = "Monday";
    weekday[2] = "Tuesday";
    weekday[3] = "Wednesday";
    weekday[4] = "Thursday";
    weekday[5] = "Friday";
    weekday[6] = "Saturday";
    
    var currentDay = weekday[currentDate.getDay()];
      
    var currentDayID = "#" + currentDay; //gets todays weekday and turns it into id
    $(currentDayID).toggleClass("today"); //this works at hightlighting today 

}