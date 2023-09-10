"""
Description: Script to read dataframe clean and transform.
"""
from extract import extract


def transform():
    """
    Description: Method to transform and clean dataframe.
    Input: None
    Output: data_frame (Pandas Objectdict)
    """
    data_frame = extract()
    headers = list(data_frame.columns)
    data_frame.drop_duplicates(inplace=True)
    new_headers = []
    for header in headers:
        if 'Unnamed' in header:
            data_frame.drop([header],axis=1,inplace=True)
        else:
            new_headers.append(header.replace(' ','_'))
    data_frame = data_frame.tail(-1)
    data_frame.columns = new_headers
    return data_frame


