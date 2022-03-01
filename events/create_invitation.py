import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from argparse import ArgumentParser
from icalendar import Calendar, Event
from dateparser import parse
from datetime import datetime, timezone, timedelta


load_dotenv()


def main() -> int:
    template = os.environ.get("TEMPLATE_FILE", "invitation_template.txt")
    zoom_link = os.environ.get("ZOOM_LINK", "<fill in zoom link>")
    timezone_id = 'Europe/Helsinki'

    parser = ArgumentParser()
    parser.add_argument("date", type=str)
    parser.add_argument("presenter", type=str)
    parser.add_argument("topic", type=str)
    parser.add_argument("--zoom", type=str, default=zoom_link)
    parser.add_argument("--template", type=str, default=template)
    args = parser.parse_args()

    parsed_date = parse(args.date, settings={'TIMEZONE': timezone_id, 'DATE_ORDER': 'DMY'}, languages=['fi', 'en'])
    #print(f"Original date: {args.date}")
    #print("  Parsed date: {}".format(parsed_date.strftime("%a %b %-d, %Y at %H:%M")))

    template = Path(args.template)
    if not template.is_file():
        print(f"Could not find template file at: {template}.")
        return -1

    print("#### INVITATION STARTS ####\n")
    with open(template) as template_file:
        template_str = "".join(template_file.readlines())
        template_filled = template_str.format(date=parsed_date.strftime("%a %b %-d, %Y at %H:%M"), presenter=args.presenter, topic=args.topic, zoom_link=args.zoom)
        print(template_filled)
    print("\n#### INVITATION ENDS ####\n")

    def display(cal):
        return cal.to_ical().replace('\r\n', '\n').strip()

    cal = Calendar()
    cal.add('prodid', '-//Python Club Calendar Tool//pythonclubcalendartool.turqoosi.net//')
    cal.add('version', '2.0')
    cal.add('calscale', 'GREGORIAN')
    cal.add('tzid', timezone_id)

    event = Event()
    event.add('created', datetime.now())
    event.add('dtstart', parsed_date, parameters={'TZID': timezone_id})
    event.add('dtend', parsed_date+timedelta(hours=1), parameters={'TZID': timezone_id})
    event.add('summary', f"Python Club: {args.topic}")
    event.add('description', template_filled)
    event['location'] = args.zoom

    cal.add_component(event)
    ical = cal.to_ical()
    ical_str = ical.replace(b'\r\n', b'\n').strip().decode()

    print("#### CAL.ICS STARTS ####\n")
    print(ical_str)
    print("\n#### CAL.ICS ENDS ####\n")

    ical_filename = Path(parsed_date.strftime("Python_Club_%Y%m%d_%H%M.ics"))
    if ical_filename.is_file():
        print(f"ERROR: File {ical_filename} already exists. Refusing to overwrite.")
        sys.exit(-1)

    with open(ical_filename, 'w') as file:
        file.write(ical_str)


if __name__ == "__main__":
    sys.exit(main())

