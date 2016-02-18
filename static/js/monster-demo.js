jQuery.noConflict();
jQuery(document).ready(function($) {
    $("#monster-demo").load(function() {
        $("#monster-demo").loadgo({
            'direction': 'bt'
        });
    }).each(function() {
        if(this.complete) $(this).load();
    });

    $("#increase-percentage").click(function (e) {
        e.preventDefault();
        var $image = $('#monster-demo'),
            step = parseInt($("#step").val()),
            currentStr = String($image.loadgo('getprogress')),
            current = parseFloat(currentStr, 10),
            newValue = 0;

        console.log(current, step, currentStr);

        if (current < 100) {
            newValue = current + step;
        } else if (current == 100) {
            newValue = 0; // Reset if full.
        }

        $image.loadgo('setprogress', newValue);
    });

    $("#decrease-percentage").click(function (e) {
        e.preventDefault();
        var $image = $('#monster-demo'),
            step = parseInt($("#step").val()),
            currentStr = String($image.loadgo('getprogress')),
            current = parseFloat(currentStr, 10),
            newValue = 0;

        if (current > 0) {
            newValue = current - step;
        }

        $image.loadgo('setprogress', newValue);
    });

    $("#reset").click(function (e) {
        e.preventDefault();
        $('#monster-demo').loadgo('resetprogress');
    });
});