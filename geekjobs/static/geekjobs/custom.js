$('#jobs-table').bootstrapTable({
  data: jobs,
  showHeader: false,
  pagination: true,
  pageSize: 10,
  detailView: true,
  detailFormatter: function displaySummary (index, row, element) {
    if (row.instructions) {
      return '<div class="well">'
      + row.summary
      + '<br><p><strong>How to apply:</strong></p><br><p>'
      + row.instructions + '</p>'
      + '</div>'
    } else {
      return '<div class="well">'
      + row.summary
      + '<br><p><strong>How to apply:</strong></p><br><p>'
      //+ '<a target="_blank" href="'+ row.link +'"> Apply via StackOverflow.' + '</p>'
      + '<a class="btn btn-primary btn-lg" href="'+ row.link +'"><strong> Apply here </strong></a>'
      + '</div>'
    }
  },
  iconSize: "xs",
  classes: "table table-no-bordered borderless",
  // cardView: true,
  // smartDisplay: false,

  rowStyle: function rowStyle(row, index) {
    return {
      css: {"font-size": "14px"}
    }
  },

  columns: [{
    field: 'title',
    formatter: function rowFormatter(value, row, index) {
      // return row.title + " " + row.author
      if (row.featured) {
          return '<address><a class="here active"><strong>' + row.title
          +  '</strong></a><br><small class="text-muted">' + row.author + ' | '
          + row.days + ' days ago</small></address>'
      } else {
          return '<address><a class="here"><strong>' + row.title
          +  '</strong></a><br><small class="text-muted">' + row.author + ' | '
          + row.days + ' days ago</small></address>'
      }

    }
  }],

  onClickRow: function(row, element){
        $(element[0]).find('.detail-icon').triggerHandler("click")}
});


$(document).ready(function(){
     $(window).scroll(function () {
            if ($(this).scrollTop() > 50) {
                $('#back-to-top').fadeIn();
            } else {
                $('#back-to-top').fadeOut();
            }
        });
        // scroll body to 0px on click
        $('#back-to-top').click(function () {
            $('#back-to-top').tooltip('hide');
            $('body,html').animate({
                scrollTop: 0
            }, 800);
            return false;
        });

        $('#back-to-top').tooltip('show');

});