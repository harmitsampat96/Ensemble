// bar chart data
var barData = {
labels : [
  {% for item in labels %}
    "{{ item }}",
  {% endfor %}
],
datasets : [{
  fillColor: "rgba(151,187,205,0.2)",
  strokeColor: "rgba(151,187,205,1)",
  pointColor: "rgba(151,187,205,1)",
  pointStrokeColor: "#fff",
  pointHighlightFill: "#fff",
  pointHighlightStroke: "rgba(151,187,205,1)",
  bezierCurve : false,
  data : [
    {% for item in values %}
      {{ item }},
    {% endfor %}
  ]
}]
}
Chart.defaults.global.animationSteps = 50;
Chart.defaults.global.tooltipYPadding = 16;
Chart.defaults.global.tooltipCornerRadius = 0;
Chart.defaults.global.tooltipTitleFontStyle = "normal";
Chart.defaults.global.tooltipFillColor = "rgba(0,0,0,0.8)";
Chart.defaults.global.animationEasing = "easeOutBounce";
Chart.defaults.global.responsive = false;
Chart.defaults.global.scaleLineColor = "black";
Chart.defaults.global.scaleFontSize = 16;
// get bar chart canvas
var mychart = document.getElementById("chart").getContext("2d");
steps = 10
max = {{ max }}
// draw bar chart
var LineChartDemo = new Chart(mychart).Line(barData, {
scaleOverride: true,
scaleSteps: steps,
scaleStepWidth: Math.ceil(max / steps),
scaleStartValue: 0,
scaleShowVerticalLines: true,
scaleShowGridLines : true,
barShowStroke : true,
scaleShowLabels: true,
bezierCurve: false,
});

let myChart = document.getElementById('myChart').getContext('2d');

// Global Options
Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = '#777';

let massPopChart = new Chart(myChart, {
  type:'doughnut', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
  data:{
    labels:['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
    datasets:[{
      label:'Population',
      data:[
        617594,
        181045,
        153060,
        106519,
        105162,
        95072
      ],
      //backgroundColor:'green',
      backgroundColor:[
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ],
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    }]
  },
  options:{
    title:{
      display:true,
      text:'Largest Cities In Massachusetts',
      fontSize:25
    },
    legend:{
      display:true,
      position:'right',
      labels:{
        fontColor:'#000'
      }
    },
    layout:{
      padding:{
        left:50,
        right:0,
        bottom:0,
        top:0
      }
    },
    tooltips:{
      enabled:true
    }
  }
});