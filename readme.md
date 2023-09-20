# PBCrawler

Small script to scrape categories or individual products from the fast fashion retailer Pull and Bear using the hidden API. The resulting JSON files carry a lot of information and probably need to be preprocessed depending on use.

## Installation

Full list of requirements can be found in requirements.txt
The only packages I installed were "requests" and "fake_useragent"

## Usage

The script requires three arguments

1) --store: the country of the store you want to scrape from

2) --language: language of data, note that only local languages and English are supported

3) --choice: "category" or "product". For category first enter the gender and then enter one of the displayed categories. For product enter a list of product IDs separated by spaces. Note that product IDs can be found in their respective URLs.

info.json contains category names and fields required for the API

## Contributing

Pull requests and criticism are welcome.

## Disclaimer

This web crawler is intended for educational and research purposes only. It is designed to retrieve publicly accessible information from websites in a respectful and non-invasive manner. 

I do not endorse or promote any illegal, harmful, or unethical activities and assume no responsibility for any legal consequences or ethical issues that may arise from its use. Users are urged to exercise caution, respect the rights and policies of websites they crawl, and use the tool responsibly. Users are responsible for ensuring that their usage complies with all applicable laws and regulations

By using this web crawler, you agree to abide by its intended usage and acknowledge that any misuse or violation of applicable laws and regulations is solely your responsibility.

Please use responsibly.

## License

[MIT](https://choosealicense.com/licenses/mit/)