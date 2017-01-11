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
      + '<a href="'+ row.link +'"> Apply via StackOverflow.' + '</p>'
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
  }]
});
