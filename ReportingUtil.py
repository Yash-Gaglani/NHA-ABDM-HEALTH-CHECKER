import json
from typing import List

from FeatureHealth import FeatureHealth


def create_paragraph(text):
    return f'<p style="font-family: Helvetica; font-size: 12pt">{text}</p>'


def generate_report(feature_health_list: List[FeatureHealth]):
    # Create an HTML file
    html_filename = "abdm_feature_health_report.html"

    # Create the HTML content
    html_content = '<html><head><style> \
        table { \
            border-collapse: collapse; \
            width: 100%; \
        } \
        .fail { \
            background: red; \
        } \
        .pass { \
            background: green; \
        } \
        .wrap { \
            max-width: 200px; \
            overflow-wrap: break-word; \
            text-align: left; \
            white-space: normal; /* Enable word wrapping for cell content */ \
        } \
    </style></head><body>'

    html_content += f'<table border="1" cellspacing="0" cellpadding="5" >'
    # Add header
    html_content += f'<tr><td>{"Feature"}</td>' \
                    f'<td>{"Status"}</td>' \
                    f'<td>{"Request URL"}</td>' \
                    f'<td>{"Request Params"}</td>' \
                    f'<td>{"Method"}</td>' \
                    f'<td>{"Request Body"}</td>' \
                    f'<td>{"Request Headers"}</td>' \
                    f'<td>{"Response Status"}</td>' \
                    f'<td>{"Response Body"}</td>' \
                    f'<td>{"Response Headers"}</td></tr>'

    # Add data from FeatureHealth objects to the HTML content
    for feature_health in feature_health_list:
        # Add feature and status cells only when they change
        html_content += f'<tr>'
        html_content += f'<td rowspan="{len(feature_health.api_calls)}"> {feature_health.feature}</td>'
        if feature_health.status == FeatureHealth.FAILING:
            html_content += f'<td rowspan="{len(feature_health.api_calls)}" class="fail"> {feature_health.status}'
        else:
            html_content += f'<td rowspan="{len(feature_health.api_calls)}" class="pass"> {feature_health.status}'
        html_content += f'</td>'

        # Loop through ApiCalls for the current feature
        first = True
        for api_call in feature_health.api_calls:
            if not first:
                html_content += f'<tr>'
            html_content += f'<td>{api_call.baseurl + api_call.endpoint}</td>' \
                            f'<td class="wrap">{api_call.request_params}</td>' \
                            f'<td >{api_call.method}</td>' \
                            f'<td class="wrap">{api_call.request_body}</td>' \
                            f'<td class="wrap">{api_call.request_headers}</td>' \
                            f'<td>{str(api_call.response_status)}</td>' \
                            f'<td class="wrap">{json.dumps(api_call.response_body)}</td>' \
                            f'<td class="wrap">{str(api_call.response_headers)}</td>'
            first = False
            if not first:
                html_content += f'</tr>'

        html_content += f'</tr>'

    # Close the HTML content
    html_content += '</table></body></html>'

    # Save the HTML content to a file
    with open(html_filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"HTML generated and saved as '{html_filename}'")
