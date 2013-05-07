mongo web shell README - cs132 final
====================================
For a cheap and easy testing of the the shell, it will be deployed to
[Heroku][] by the end of 5/6. Please do not make malicious queries (i.e.
inserting the whole world into the database) - this is 10gen's repo.

Note that we are also doing a little bit of extra work to make the code handoff
to 10gen smooth so the version on Heroku may be an improved version over what
we've handed in.

If you'd like to run the code locally, README.md should be sufficient to get
you started.

You can view our presentation slides on [Google Docs][], which is probably the
best resource for implementation details (beyond the source itself).

Project layout
--------------
Our backend code is located within the mongows/ dir. Our main deliverable is
the web shell, which is handled in the mongows/mws/ Flask Blueprint. This shell
can be embeded in any page that serves the frontend code (and configuration
options may be specified to the frontend code to make requests to a server
other than the one that delivered the HTML content). The mongows/sample/
Blueprint, on the other hand, is a sample implementation of a server serving
the web content.

A person wishing to include the web shell on their site can either use their
existing server or register a new Flask Blueprint within our mongows
application to serve the content. standalone\_sample/ is an unmaintained
example of the former.

The frontend code is located in the frontend/ dir.

Tests for the backend are located in tests/ and tests for the frontend are
located in frontend/spec/.

Additional documentation can be found in the docs/ dir.

Meeting specs/requirements
--------------------------
As is wont to happen with projects of this scale, we fell short of our expected
goals. Some things we missed:

* Omni/auto-completion
* Thorough testing (to be completed before we hand it off to 10gen)
* Additional mongo commands (update(), sort(), etc.)
    * The associated API calls
* Sufficient error handling
* Garbage collection of inactive server resources (i.e. deleting resources that
  are no longer in use) (to be completed before we hand off)
* Protection against simple malicious queries (like inserting large amounts of
  data)
* Some documentation is under spec'd (to be completed before we hand off)

You'll find that we took note of many of our issues as TODOs in the code.
Issues that were more general are located in Github Issues though it's a
private repository so you cannot gain access. However, if you would like to see
these, we can type them up and send them your way.

Code quality
------------
As we mentioned in our presentation, we REALLY took a lot of effort in making
our code both readable and maintainable. We used linters like jshint and pep8,
did code reviews for all code merged to upstream, and spent a good deal of time
refactoring already functional code for readability and maintainability.

We sacrified quantity for quality here, so we hope we get some Brownie Points.
;)

[Heroku]: http://mongo-web-shell.herokuapp.com/sample/
[Google Docs]: https://docs.google.com/presentation/d/1KV1nbZr2m32rOC_BjFDc2AyLuXDCn3jmV5HDT2tNVlg/edit#slide=id.p
