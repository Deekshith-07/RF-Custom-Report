from jinja2 import Environment, FileSystemLoader
from datetime import datetime

current_date_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def generate_html_report(
        total_passed_testcase_count: int,
        total_failed_testcase_count: int,
        total_skipped_testcase_count: int,
        total_testcase_count: int,
        total_assertion_fail_count: int,
        total_script_fail_count: int,
        total_fail_count: int,
        application_name: str,
        broswer_name: str,
        url: str,
        environment: str,
        data_source: str,
        video_recording_status: str,
        parallel_execution_status: str,
        report_path: str,
        generare_report_status: str,
        update_hisotrical_report_status: str,
        report_via_mail_status: str,
        email_ids: str,
        testcase_status_table: list,
        testcase_table: list
	):

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(r'C:\vscode\RF-Custom-Report'))
    template = env.get_template("template.html")

    # Render the template with data
    html_content = template.render(
        total_passed_testcase_count = total_passed_testcase_count,
        total_failed_testcase_count = total_failed_testcase_count,
        total_skipped_testcase_count = total_skipped_testcase_count,
        total_testcase_count = total_testcase_count,
        total_assertion_fail_count = total_assertion_fail_count,
        total_script_fail_count = total_script_fail_count,
        total_fail_count = total_fail_count,
        application_name = application_name.upper(),
        broswer_name = broswer_name,
        url = url,
        environment = environment,
        data_source = data_source,
        video_recording_status = video_recording_status,
        parallel_execution_status = parallel_execution_status,
        report_path = report_path,
        generare_report_status = generare_report_status,
        update_hisotrical_report_status = update_hisotrical_report_status,
        report_via_mail_status = report_via_mail_status,
        email_ids = email_ids,
        report_generated_date_time = current_date_time,
        testcase_status_table=testcase_status_table,
        testcase_table=testcase_table
        )

    # Write the rendered HTML to a file
    with open('test_case_report.html', 'w') as f:
        f.write(html_content)

    print("HTML file generated successfully.")

# generate_html_report(
#     	total_passed_testcase_count = 3,
#         total_failed_testcase_count = 1,
#         total_skipped_testcase_count = 1,
#         total_testcase_count = 4,
#         total_assertion_fail_count = 3,
#         total_script_fail_count = 1,
#         total_fail_count = 4,
#         application_name = "Iborg Redevelopment".upper(),
#         broswer_name = "Chrome v125.23.43",
#         url = "https://google.com",
#         environment = "Testing",
#         data_source = "Database",
#         video_recording_status = "Yes",
#         parallel_execution_status = "Yes",
#         report_path = r"C:\Users\Desktop\Reports",
#         generare_report_status = "Yes",
#         update_hisotrical_report_status = "Yes",
#         report_via_mail_status = "Yes",
#         email_ids = "deekshith.p@sirmaindia.com, swaraj.m@sirmaindia.com",
#         testcase_status_table=testcase_status_table,
#         testcase_table=testcase_table
#         )
