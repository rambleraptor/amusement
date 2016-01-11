# Getting Started
I'm always welcoming new PRs and am happy to help you in any way I can. For starters, here's what you need to do.

* Fork the repo on Github
* Make your changes on a separate branch
* Submit a Pull Request

Don't know how to do any of these things? Just ask me.

# Tests
I'm a stickler for tests. If you're fixing a bug that's not inherently obvious, please submit a test. For parks, an integration test will work just fine. The integration test should just prove that the park will assemble correctly and then has some rides or shows.

# Documentation
Documentation is always great (even for this page, which could use some serious work). Even if you have no code experience, feel free to make changes!

# New Parks
New parks are always welcome! My goal is to have every major park accounted for in amusement. I do have a couple rules for any new parks:
* All data must be gathered from **official** sources. This means that the theme park's website or mobile app. Any data collected from third-party applications (where somebody else is gathering data) is not allowed. Third party data sources + apps are never fully acurrate.
* No crowdsourced data. Crowdsourced data relies on a large, trustworthy crowd to be acurrate. I have no way of verifying either of those.

Need help building a new park? I can help more on a case-by-case basis, but here's the rough idea:
1. Find an official website or mobile app for the theme park.
2. If it's a website, you can use BeautifulSoup to scrape the website (see Universal Hollywood for examples).
3. Mobile apps are trickier. Try using MITMProxy to see the specific HTTP requests that are returning wait times.


