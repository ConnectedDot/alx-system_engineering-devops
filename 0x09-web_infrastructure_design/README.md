# Web Infrastructure Design

## Concepts
For this project, we expect you to look at these concepts:

- [DNS](#DNS)
- [Monitoring](https://en.wikipedia.org/wiki/Monitoring)
- [Web Server](#Webserver)
- [Network basics](https://www.ibm.com/topics/networking)
- Load balancer
- Server

### DNS
#### Basics
DNS is, in simple words, the technology that translates human-adapted, text-based domain names to machine-adapted, numerical-based IP:

- [Learn everything about DNS in cartoon](https://howdns.works/)
- Be sure to know the main DNS record types:
1. [A](https://support.dnsimple.com/articles/a-record/)
2. [CNAME](https://en.wikipedia.org/wiki/CNAME_record)
3. [MX](https://en.wikipedia.org/wiki/MX_record)
4. [TXT](https://en.wikipedia.org/wiki/TXT_record)

#### Advanced
- [Use DNS to scale with round-robin DNS](https://www.dnsknowledge.com/whatis/round-robin-dns/)
- [What’s an NS Record?](https://support.dnsimple.com/articles/ns-record/)
- [What’s an SOA Record?](https://support.dnsimple.com/articles/soa-record/)

#### The root domain and sub domain - differences
A root domain is the parent domain to a sub domain, and its name is not, and can not be divided by a dot.

While creating any domain at a website of domain provider, the provider system will always ask you to choose a domain name without a dot in the name. In other words, the address of the root domain may be mydomain.com but it can never be my.domain.com. Domain providers block the ability to create such a root domain until you type a name without the dot. Why?

The dot in the domain name delimits the sub domain name (the part of the name before the dot, eg. www.my.) and the root domain name ( the part after the dot, ie .domain.com). This means that the address my.domain.com is a sub domain of the root domain, whose name is domain.com

In an administrator panel at domain provider account, you can create any number of sub domains. This means that for the root domain called domain.com it is possible to create different sub domains eg. my.domain.com, your.domain.com, school.domain.com… Creating multiple sub domains is always free and does not require you to set up new accounts on a domain provider website.

As you can see, all of the domain addresses used as an example (above) do not start with the www prefix. www is also a sub domain. The www prefix always leads to the main domain. See: [What’s the point in having www in a url?](https://serverfault.com/questions/145777/what-s-the-point-in-having-www-in-a-url)


### Web server

Do not mix up web server and server.

A web server is a software that delivers web pages. A server is an actual computer.

But you might hear people referring to a web server using the word server. (Check out the server concept page to learn more about this.)

As mentioned above, a server is a physical machine, an actual computer, but in the Cloud era that could also be a virtual computer, generally called a [VM (Virtual Machine)](https://en.wikipedia.org/wiki/Virtual_machine) or [container](https://www.cio.com/article/247005/what-are-containers-and-why-do-you-need-them.html).

**Readme:**

- [Wikipedia page about web server](https://en.wikipedia.org/wiki/Web_server)
- [Web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)
- [What is a Web Server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)

## Description

This project is a collection of web infrastructure designs that could be implemented in any web development project.

## Designs Presented

+ Simple web stack - [details](0-simple_web_stack)
+ Distributed web infrastructure - [details](1-distributed_web_infrastructure)
+ Secured and monitored web infrastrucure - [details](2-secured_and_monitored_web_infrastructure)
+ Scaled up web infrastructure - [details](3-scale_up)