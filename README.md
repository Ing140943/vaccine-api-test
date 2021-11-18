# Suchon's Site API Testing

How to run the Test          
* ```python -m unittest api_testing.py```

## Detail
List of Test Cases

| # | Test Case  | Description     | Result|
|---|:----------|:------------------|---------|
| 1 | test_can_GET_all_users_path_all | Fetching data from data base, it should return list of all people correctly.  |Pass|
| 2 | test_get_user_with_valid_date | Use ```GET``` method to get the data of users in the specific date. |Pass|
| 3 | test_get_status_code_with_future_date | Use ```GET``` method to get the data of users in the future date. |Pass|
| 4 |test_get_status_code_without_num_date |  Use ```GET``` method to get the data of users on empty date.|Pass|
| 5 | test_invalid_date_format | Use ```GET``` method to get the data of users by providing invalid date format.|Pass|
| 6 | test_provide_invalid_month_in_date_format|Use ```GET``` method to get the data of users by providing invalid month in date format. |Pass|
| 7 | test_provide_slash_in_date_format | Use ```GET``` method to get the data of users by using `/` in date format.|Pass|
| 8 | test_provide_wrong_date_format |Use ```GET``` method to get the data of users by providing string in the given WEB_URL. |Pass|
| 9 | test_provide_wrong_param | Use ```GET``` method to get the data of users by providing date with wrong path.|Pass|
| 10 | test_verify_JSON_data_type_format | Checking data type from fetching data, the type should be ```JSON```|Pass|

## Conclusion
From the list of Test Cases. My test pass 6 tests and fail 4 tests.
You can see the test which fail at table above. [24 Oct 2021]

Right now all test is pass. [11 Nov 2021]