jQuery.noConflict();
jQuery(document).ready(function($) {
    $('#team-tabs').find('a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    });
    $('[data-toggle="shape-tooltip"]').tooltip({placement: 'bottom'})
});