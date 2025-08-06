from utils.logger import setup_logger
from test_data.booking_payloads import generate_booking
from utils.html_report import generate_html_report
import json

logger = setup_logger()

def test_create_bookings(api_handle, shared_booking_ids):
    booking1 = generate_booking(500, True, "lunch")
    booking2 = generate_booking(1000, False, "")
    booking3 = generate_booking(750, True, "breakfast")

    response1 = api_handle.create_booking(booking1)
    response2 = api_handle.create_booking(booking2)
    response3 = api_handle.create_booking(booking3)    

    shared_booking_ids["id1"] = response1.json().get("bookingid")
    shared_booking_ids["id2"] = response2.json().get("bookingid")
    shared_booking_ids["id3"] = response3.json().get("bookingid")
    
    logger.info("All available booking ID's")
    i = 1
    for key, booking_id in shared_booking_ids.items():
        if not booking_id:
            logger.error(f"{key} not returned!")
            assert False, f"{key} was not created successfully."
        else:
            logger.info(f"Booking{i} created with ID: {booking_id}")
            response = api_handle.get_booking_details(booking_id)
            data = json.dumps(response.json(), indent=4)
            logger.info(data)
            i += 1
        
    assert response1.status_code == 200, "Booking1 creation failed"
    assert response2.status_code == 200, "Booking2 creation failed"
    assert response3.status_code == 200, "Booking3 creation failed"

def test_modify_bookings(api_handle, shared_booking_ids):
    modify_booking1_total_price = 1000
    modify_booking2_total_price = 1500
    booking1 = generate_booking(modify_booking1_total_price, True, "lunch")
    booking2 = generate_booking(modify_booking2_total_price, False, "")

    response1 = api_handle.update_booking(shared_booking_ids["id1"], booking1)
    response2 = api_handle.update_booking(shared_booking_ids["id2"], booking2)

    updated_booking1_total_price = response1.json().get("totalprice")
    updated_booking2_total_price = response2.json().get("totalprice")

    logger.info(f"Booking1 updated with total price = {updated_booking1_total_price}")
    logger.info(f"Booking2 updated with total price = {updated_booking2_total_price}")

    assert response1.status_code == 200
    assert modify_booking1_total_price == updated_booking1_total_price
    assert response2.status_code == 200
    assert modify_booking2_total_price == updated_booking2_total_price

def test_delete_booking(api_handle, shared_booking_ids):
    booking_id = shared_booking_ids["id3"]
    response = api_handle.delete_booking(booking_id)

    logger.info(f"Deleted booking id = {booking_id} and status = {response.status_code}")

    assert response.status_code == 201

def test_generate_report():
    generate_html_report()
    logger.info("HTML report generated as report.html")
