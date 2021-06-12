var myConfig = {
    type: 'radar',
    plot: {
      aspect: 'area',
      animation: {
        effect: 3,
        sequence: 1,
        speed: 700
      }
    },
    scaleV: {
      visible: false
    },
    scaleK: {
      values: '0:5:1',
      labels: ['Dogs', 'Cats', 'Fish', 'Birds', 'Reptiles', 'Horses'],
      item: {
        fontColor: '#607D8B',
        backgroundColor: "white",
        borderColor: "#aeaeae",
        borderWidth: 1,
        padding: '5 10',
        borderRadius: 10
      },
      refLine: {
        lineColor: '#c10000'
      },
      tick: {
        lineColor: '#59869c',
        lineWidth: 2,
        lineStyle: 'dotted',
        size: 20
      },
      guide: {
        lineColor: "#607D8B",
        lineStyle: 'solid',
        alpha: 0.3,
        backgroundColor: "#c5c5c5 #718eb4"
      }
    },
    series: [{
        values: [59, 39, 38, 19, 21, 35],
        text: 'farm'
      },
      {
        values: [20, 20, 54, 41, 41, 35],
        lineColor: '#53a534',
        backgroundColor: '#689F38'
      }
    ]
  };
   
  zingchart.render({
    id: 'myChart',
    data: myConfig,
    height: '100%',
    width: '100%'
  });