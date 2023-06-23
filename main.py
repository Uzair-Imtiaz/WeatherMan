from ReportGenerator import ReportGenerator
from arg_parser import parse_args


def main():
    """
    The main function.

    Receives command line arguments by calling the arg_parse function and then call the generate_report function.
    """

    args = parse_args()
    rg = ReportGenerator()
    rg.generate_report(args.files_dir, args.year_and_month_for_a, args.year_and_month_for_c, args.year)


if __name__ == '__main__':
    main()
