#!/usr/bin/env python3

# Created by: Rohnin. B
# Created on: Sep 2021
# this program formats your adress to a mailing adress


def adress_formater(
    full_name,
    apartment_answer,
    street_number_int,
    street_name,
    city_name,
    province_name,
    postal_code,
    apartment_number_int=None,
):

    # this function formats your adress to a mailing adress

    apt_street_num = ""
    if apartment_answer == "y":
        apt_street_num = "{0}-{1}".format(apartment_number_int, street_number_int)
    else:
        apt_street_num = street_number_int

    adress = "\n{0}\n{1} {2}\n{3} {4}  {5}".format(
        full_name, apt_street_num, street_name, city_name, province_name, postal_code
    )
    adress = adress.upper()

    return adress


def main():
    # this function gets adress, full_name, apartment_answer, street_number,
    #   street_name, city_name, province_name, postal_code, apartment_number

    apartment_number_int = None

    # input
    full_name = input("Enter your full name: ")

    apartment_answer = input("Do you live in an apartment? (y/n): ")
    if apartment_answer == "y":
        apartment_number = input("Enter your apartment number: ")
    else:
        apartment_number = None

    street_number = input("Enter your street number :")
    street_name = input("Enter your street name AND type ex: Main St: ")
    city_name = input("Enter your city name: ")
    province_name = input("Enter your province (as an abreviation ex: ON, BC ect.) :")
    postal_code = input("Enter your postal code (ex: A1B 2C3): ")

    try:
        street_number_int = int(street_number)
        if apartment_number != None:
            apartment_number_int = int(apartment_number)

        adress_formated = adress_formater(
            full_name,
            apartment_answer,
            street_number_int,
            street_name,
            city_name,
            province_name,
            postal_code,
            apartment_number_int,
        )

        print(adress_formated)
    except Exception as e:
        print("\nInvalid Input {}".format(e))

    print("\nDone.")


if __name__ == "__main__":
    main()
