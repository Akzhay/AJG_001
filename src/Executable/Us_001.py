import sys,os
sys.path.insert(1, '../Gall_01')
print(sys.path)
from src.Database.database import connect_to_database   

def check_coverage_code(database, coverage_code):
    cursor = database.cursor()
    cursor.execute('SELECT code FROM coverage_codes WHERE code = ?', (coverage_code,))
    result = cursor.fetchone()

    if not result:
        coverage_code = 'P'
        cursor.execute('SELECT code FROM coverage_codes WHERE code = ?', (coverage_code,))
        result = cursor.fetchone()
        
        if not result:
            coverage_type = 'international coverage'
        else:
            coverage_type = 'split coverage'
    else:
        coverage_type = 'valid coverage'

    return coverage_code, coverage_type

def process_claim_details(database, claim_details, ws_activity_from_date, ws_activity_to_date):
    # Initialize variables
    dxq82_reserve_category = 0
    dxq82_return_code = 0
    ws_bypass_claim_flag = False
    ws_dtclmsn_void_yes = False
    ws_dtclmsn_void_no = False
    ws_ctr_dtclmsn = 0
    
    # Check if claim detail trap SN exists
    if claim_details.get('DTCLMSN_CLM_DTL_TRAP_SN'):
        if claim_details.get('DTCLMSN_STATUS_CODE') == "VO":
            if ws_activity_from_date < claim_details.get('DTCLMSN_ORIG_OPEN_DATE') < ws_activity_to_date:
                ws_bypass_claim_flag = True
            else:
                ws_dtclmsn_void_yes = True
        else:
            ws_dtclmsn_void_no = True
        
        # Perform the check converted claim routine
        # This is a placeholder for the actual routine
        perform_check_converted_claim()

        if ws_bypass_claim_flag:
            return ws_ctr_dtclmsn
        else:
            ws_ctr_dtclmsn += 1

    return ws_ctr_dtclmsn

def perform_check_converted_claim():
    # Placeholder function for the 100-75-CHECK-CONVERTED-CLAIM routine
    pass

# Example usage
coverage_code = 'X'
conn = connect_to_database('example.db')
coverage_code, coverage_type = check_coverage_code(conn, coverage_code)
print(f'Coverage Code: {coverage_code}, Coverage Type: {coverage_type}')

claim_details = {
    'DTCLMSN_CLM_DTL_TRAP_SN': 1,
    'DTCLMSN_STATUS_CODE': 'VO',
    'DTCLMSN_ORIG_OPEN_DATE': '2023-06-01'
}

ws_activity_from_date = '2023-01-01'
ws_activity_to_date = '2023-12-31'


ws_ctr_dtclmsn = process_claim_details(conn, claim_details, ws_activity_from_date, ws_activity_to_date)
print(f'Counter of processed claim details: {ws_ctr_dtclmsn}')
