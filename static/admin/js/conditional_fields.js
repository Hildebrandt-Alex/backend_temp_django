django.jQuery(document).ready(function($) {
    function updateConditionalFields() {
        var widgetType = $('#id_widget_type').val();
        $('.field-custom_html').toggle(widgetType === 'custom_html');
        $('.field-num_posts').toggle(widgetType === 'latest_posts');
    }

    $('#id_widget_type').change(updateConditionalFields);
    updateConditionalFields(); // Initial beim Laden der Seite aufrufen
});