jQuery(document).ready(function($) {
    /* mobile menu */
    $(".menu-icon").click(function(){
        $(".nav-links").fadeToggle();
        $(this).toggleClass("in");
    });
    /* user account menu */
    $(".user-link").click(function(){
        $(".user-dropdown").fadeToggle();
    });
    /* card drag */
    $( ".sortable" ).sortable({
        connectWith: ".task-wrapper",
        stack: '.task-wrapper',
        placeholder: 'sortable-placeholder'
    }).disableSelection();

    /* table drag */
    $(".sort-table").dragtable({
        dragaccept: '.draggable-col',
        dragHandle: '.drag-handle'          
    });
    /* table asc-desc sorting */
    $('.sort-table').on('click', '.sortbale-col', function () {
      var index = $(this).index(),
          rows = [],
          thClass = $(this).hasClass('asc') ? 'desc' : 'asc';

      $('.sort-table th').removeClass('asc desc');
      $(this).addClass(thClass);

      $('.sort-table tbody tr').each(function (index, row) {
        rows.push($(row).detach());
      });

      rows.sort(function (a, b) {
        var aValue = $(a).find('td').eq(index).find(".sort-value").text(),
            bValue = $(b).find('td').eq(index).find(".sort-value").text();

        return aValue > bValue
            ? 1
            : aValue < bValue
            ? -1
            : 0;
      });

      if ($(this).hasClass('desc')) {
        rows.reverse();
      }

      $.each(rows, function (index, row) {
        $('.sort-table tbody').append(row);
      });
    });

    /* display tabs toggle */
    $(".display-tab button").click(function(e){
        $(".display-tab button").not(this).removeClass("focused");
        $(this).addClass("focused");
        $(".display-wrapper").hide();
        var display = $(this).data("target");
        if($(this).data("display-tab") == 2)
            $(".display-tab").addClass("active-tab2");
        else
            $(".display-tab").removeClass("active-tab2");
        $("#"+display).fadeIn();
    });

    /* Card properties and rounds toggle */
    $('.switchbtn input[type="checkbox"]').click(function(){
        var inputValue = $(this).val();
        $("[data-app-class = "+inputValue+"]").slideToggle();
    });

    /* Header right icons active and hover css */
    $(".header-icon").hover(function(){
        $(this).children("i").addClass("in");
    },
    function(){
        $(this).children("i").removeClass("in");
    });

    /* Search bar toggle */
    $(".header-search").click(function(){
        $(".header-search-wrapper").addClass("in");
    });
    $(".close-search").click(function(){
        $(".header-search-wrapper").removeClass("in");
    });

    /* header icon dropdown toggle */
    $(".setting-more").click(function(){
        $(".setting-menu").not($(this).next()).hide();
        $(this).next(".setting-menu").fadeToggle(100);
        $(".card-prop-menu").hide();
    });
    $(".card-prop-more").click(function(){
        $(this).siblings(".card-prop-menu").show();
    });
    $(".card-prop-back").click(function(){
        $(this).parent(".card-prop-menu").hide();
    });

    /* close dropdown menu after clicking outside */
    $(document).mousedown(function (e){
        var click_source = $(".setting-more,.more-icon");
        if(click_source.is(e.target)){
            return false;
        }
        var toggle_div = $(".setting-menu,.more-menu");
        if (!toggle_div.is(e.target) && toggle_div.has(e.target).length === 0){
            toggle_div.hide();            
        }
    });

    /* edit/delete menu toggle */
    $(".more-icon").click(function(){
        $(".more-menu").not($(this).next()).hide();
        $(this).next(".more-menu").toggle();
    });

    /* open modal */
    $('.modal-toggle').on('click', function(e) {
        e.preventDefault();
        $('.modal').fadeToggle().toggleClass('is-visible');
    });

    /* disable future dates on HTML5 datepicker */
    var dtToday = new Date();
    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();
    var maxDate = year + '-' + month + '-' + day;    
    $('.disable-future-dates').attr('max', maxDate);
    
});