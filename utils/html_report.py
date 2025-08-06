def generate_html_report(log_file='booking.log', output_file='report.html'):
    with open(log_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        f.write("<html><head><title>Booking Report</title></head><body>")
        f.write("<h2>Booking Automation Report</h2><pre>")
        for line in lines:
            f.write(line)
        f.write("</pre></body></html>")
