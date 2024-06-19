from jinja2 import Environment, FileSystemLoader
from datetime import datetime

current_date_time = datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")

# Sample data
testcase_status_table = [
		{
			"SerialNum": "",
			"TestCaseID": "TC01",
			"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
			"ExecutionStartTime": "06:51:21 PM",
			"Duration": "28 sec",
			"Status": "FAILED",
			"ErrorType": "Assertion/Script Error",
			"Reason": "Check point got failed since excepcted : 'Username Admin1' and actual : 'Username Admin' values are not matched,",
			"StepNum": "Step-1"
		}
	]

testcase_table = [
			{
				"SerialNum": "1",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-1",
				"Steps": "Navigate to URL",
				"ExecutionStartTime": "06:51:22 PM",
				"Duration": "11 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "2",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-2",
				"Steps": "Verify Page Title",
				"ExecutionStartTime": "06:51:33 PM",
				"Duration": "0 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "3",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-3",
				"Steps": "Reload",
				"ExecutionStartTime": "06:51:33 PM",
				"Duration": "1 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "4",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-4",
				"Steps": "Wait for Element - LoginPageHeader",
				"ExecutionStartTime": "06:51:34 PM",
				"Duration": "1 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "5",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-5",
				"Steps": "Verify Text - UsernameText",
				"ExecutionStartTime": "06:51:35 PM",
				"Duration": "2 sec",
				"Status": "FAILED",
				"ErrorType": "Assertion Error",
				"Reason": "Check point got failed since excepcted : 'Username Admin1' and actual : 'Username Admin' values are not matched."
			},
			{
				"SerialNum": "6",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-6",
				"Steps": "Verify Text Contains - PasswordText",
				"ExecutionStartTime": "06:51:38 PM",
				"Duration": "0 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "7",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-7",
				"Steps": "Verify Text Starts With - UsernameText",
				"ExecutionStartTime": "06:51:38 PM",
				"Duration": "0 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "8",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-8",
				"Steps": "Verify Text Ends With - PasswordText",
				"ExecutionStartTime": "06:51:38 PM",
				"Duration": "1 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "9",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-9",
				"Steps": "Input Data - UsernameField",
				"ExecutionStartTime": "06:51:39 PM",
				"Duration": "1 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "10",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-10",
				"Steps": "Input Data - PasswordField",
				"ExecutionStartTime": "06:51:40 PM",
				"Duration": "0 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "11",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-11",
				"Steps": "Clear Text Field - UsernameField",
				"ExecutionStartTime": "06:51:40 PM",
				"Duration": "2 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "12",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-12",
				"Steps": "Input Data - UsernameField",
				"ExecutionStartTime": "06:51:42 PM",
				"Duration": "1 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "13",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-13",
				"Steps": "Click - LoginButton",
				"ExecutionStartTime": "06:51:43 PM",
				"Duration": "2 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "14",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-14",
				"Steps": "Element Should Be Present - Dashboard",
				"ExecutionStartTime": "06:51:21 PM",
				"Duration": "25 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			},
			{
				"SerialNum": "15",
				"TestCaseID": "TC01",
				"TestCaseDesc": "Check basic web keywords on Orange HRM site1",
				"StepNum": "Step-15",
				"Steps": "Browser Close",
				"ExecutionStartTime": "06:51:46 PM",
				"Duration": "4 sec",
				"Status": "PASSED",
				"ErrorType": "",
				"Reason": ""
			}
		]

def generate_html_report():
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Render the template with data
    html_content = template.render(
        total_passed_testcase_count = 3,
        total_failed_testcase_count = 1,
        total_skipped_testcase_count = 1,
        total_testcase_count = 4,
        total_assertion_fail_count = 3,
        total_script_fail_count = 1,
        total_fail_count = 4,
        application_name = "Iborg Redevelopment".upper(),
        broswer_name = "Chrome v125.23.43",
        url = "https://google.com",
        environment = "Testing",
        data_source = "Database",
        video_recording_status = "Yes",
        parallel_execution_status = "Yes",
        report_path = r"C:\Users\Desktop\Reports",
        generare_report_status = "Yes",
        update_hisotrical_report_status = "Yes",
        report_via_mail_status = "Yes",
        email_ids = "deekshith.p@sirmaindia.com, swaraj.m@sirmaindia.com",
        report_generated_date_time = current_date_time,
        testcase_status_table=testcase_status_table,
        testcase_table=testcase_table
        )

    # Write the rendered HTML to a file
    with open('output.html', 'w') as f:
        f.write(html_content)

    print("HTML file generated successfully.")

generate_html_report()
