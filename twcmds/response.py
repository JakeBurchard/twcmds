#!/usr/bin/env python
def update_response(api, response, truncate):
    if not truncate:
        if len(response) <= 128:
            api.update_status("Computer: " + response)
        else:
            resp_list = []
            while response:
                resp_list.insert(0, "Computer: " + response[:128] + (response[128:] and '..'))
                response = response[128:]
            for resp in resp_list:
                api.update_status(resp)
    else:
        resp = "Computer: " + response[:128] + (response[128:] and '..')
        api.update_status(resp)
			
