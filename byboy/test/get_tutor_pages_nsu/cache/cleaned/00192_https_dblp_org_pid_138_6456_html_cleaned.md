> 抓取来源：https://dblp.org/pid/138/6456.html

[![Schloss Dagstuhl - Leibniz Center for Informatics](https://dblp.org/img/lzi-logo.82x57.png)](https://www.dagstuhl.de/en)

![](https://dblp.org/img/logo.320x120.png)

![search dblp](https://dblp.org/img/search.dark.16x16.png)

![search dblp](https://dblp.org/img/search.dark.16x16.png)

**default search action**

- combined dblp search
- author search
- venue search
- publication search

**Authors:**

- _no matches_

- ![waiting...](https://dblp.org/img/waiting.anim.gif)

**Venues:**

- _no matches_

- ![waiting...](https://dblp.org/img/waiting.anim.gif)

**Publications:**

- _no matches_

- ![waiting...](https://dblp.org/img/waiting.anim.gif)

![clear](https://dblp.org/img/clear-mark.medium.16x16.png)

[![ask others](https://dblp.org/img/search-external.dark.hollow.16x16.png)](https://google.com/search)

**ask others**

- [![](https://dblp.org/img/google.dark.16x16.png)Google](https://google.com/search)
- [![](https://dblp.org/img/google-scholar.dark.16x16.png)Google Scholar](https://scholar.google.com/scholar)
- [![](https://dblp.org/img/semscholar.dark.16x16.png)Semantic Scholar](https://www.semanticscholar.org/search)
- [![](https://dblp.org/img/internetarchive.dark.16x16.png)Internet Archive Scholar](https://scholar.archive.org/search)
- [![](https://dblp.org/img/citeseer.dark.16x16.png)CiteSeerX](https://citeseerx.ist.psu.edu/search_result?query=)
- [![](https://dblp.org/img/orcid.dark.16x16.png)ORCID](https://orcid.org/orcid-search/search)

This is just a _disambiguation page_, and is not intended to be the bibliography of an actual person. Any publication listed on this page has not been assigned to an actual author yet. If you know the true author of one of the publications listed below, you are welcome to [contact us.](https://dblp.org/db/about/team.html)

- [Jin-Yu Yang](https://dblp.org/pid/221/8197.html)
- [Jinyue Yang](https://dblp.org/pid/179/8196.html)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Jinyu+Yang%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Jinyu+Yang+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Jinyu+Yang+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Jinyu+Yang%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Jinyu+Yang+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Jinyu+Yang%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Jinyu+Yang%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F138%2F6456%3E+%7D+.%0A%0A%7D)

_showing all107 records_

20142025202014: 22014: 22017: 32018: 72018: 72018: 72019: 42020: 112020: 112020: 112021: 102021: 102022: 142022: 142022: 142023: 102023: 102023: 102024: 282024: 282024: 282025: 182025: 182025: 18

**refine by search term**

![](https://dblp.org/img/clear-mark.medium.16x16.png)![filter active](https://dblp.org/img/filter-mark.12x12.png)

**refine by type**

- [ ] Journal Articles(only)
- [ ] Conference and Workshop Papers(only)
- [ ] Informal and Other Publications(only)

- select all \| deselect all

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by coauthor**

- ![](https://dblp.org/img/add-mark.12x12.png)Feng Zheng 0001 (32)
- ![](https://dblp.org/img/add-mark.12x12.png)Junzhou Huang (19)
- ![](https://dblp.org/img/add-mark.12x12.png)Ales Leonardis (18)
- ![](https://dblp.org/img/add-mark.12x12.png)Mingqi Gao 0003 (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Chaochao Yan (11)
- ![](https://dblp.org/img/add-mark.12x12.png)Son Tran (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhe Li 0008 (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Peilin Zhao (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Joni-Kristian Kämäräinen (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Trishul Chilimbi (8)

- _601 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (83)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-7004-3570 (10)
- ![](https://dblp.org/img/add-mark.12x12.png)0009-0006-3567-6299 (6)
- ![](https://dblp.org/img/add-mark.12x12.png)0009-0007-5467-0690 (2)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-9765-9009 (1)
- ![](https://dblp.org/img/add-mark.12x12.png)0009-0006-5367-094X (1)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-8907-9541 (1)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0003-0769-1046 (1)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-7328-9560 (1)
- ![](https://dblp.org/img/add-mark.12x12.png)0009-0000-7555-2211 (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (37)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (13)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (9)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Briefings Bioinform. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (3)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Image Process. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)CIKM (3)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Circuits Syst. Video Technol. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)MM (3)
- ![](https://dblp.org/img/add-mark.12x12.png)WACV (2)

- _30 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (59)
- ![](https://dblp.org/img/add-mark.12x12.png)open (47)
- ![](https://dblp.org/img/add-mark.12x12.png)unavailable (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j28\]
[Chunyan Wang](https://dblp.org/pid/287/5495.html), Jinyu Yang:

Group Strong Orthogonal Arrays with Appealing Two-Dimensional Space-Filling Property. [J. Syst. Sci. Complex.38(4)](https://dblp.org/db/journals/jossac/jossac38.html#journals/jossac/WangY25): 1747-1765 (2025)
- ![](https://dblp.org/img/n.png)

\[j27\]
Jinyu Yang, [Yanjiao Shi](https://dblp.org/pid/154/1947.html), [Ying Jiang](https://dblp.org/pid/42/1709.html), [Zixuan Lu](https://dblp.org/pid/231/6422.html), [Yugen Yi](https://dblp.org/pid/147/8410.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Contextual feature fusion and refinement network for camouflaged object detection. [Int. J. Mach. Learn. Cybern.16(3)](https://dblp.org/db/journals/mlc/mlc16.html#journals/mlc/YangSJLY25): 1489-1505 (2025)
- ![](https://dblp.org/img/n.png)

\[j26\]
[Jiacheng Hou](https://dblp.org/pid/226/4634.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Bidirectional Error-Aware Fusion Network for Video Inpainting. [IEEE Trans. Circuits Syst. Video Technol.35(1)](https://dblp.org/db/journals/tcsv/tcsv35.html#journals/tcsv/HouJYZ25): 577-588 (2025)
- ![](https://dblp.org/img/n.png)

\[j25\]
[Yixuan Yang](https://dblp.org/pid/229/1326.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Zixiang Zhao](https://dblp.org/pid/65/5420.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Victor Sanchez](https://dblp.org/pid/96/2574.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

RefComp: A Reference-Guided Unified Framework for Unpaired Point Cloud Completion. [IEEE Trans. Multim.27](https://dblp.org/db/journals/tmm/tmm27.html#journals/tmm/YangYZSZ25): 9788-9801 (2025)
- ![](https://dblp.org/img/n.png)

\[c42\]
Jinyu Yang, [Ruijia Wang](https://dblp.org/pid/138/8168.html), [Cheng Yang](https://dblp.org/pid/49/1457-2.html), [Bo Yan](https://dblp.org/pid/63/6796.html), [Qimin Zhou](https://dblp.org/pid/220/1007.html), [Yang Juan](https://dblp.org/pid/299/4372.html), [Chuan Shi](https://dblp.org/pid/64/3041-1.html):

Harnessing Language Model for Cross-Heterogeneity Graph Knowledge Transfer. [AAAI2025](https://dblp.org/db/conf/aaai/aaai2025.html#conf/aaai/YangW0YZJ025): 13026-13034
- ![](https://dblp.org/img/n.png)

\[c41\]
[Chuong Huynh](https://dblp.org/pid/289/7090.html), Jinyu Yang, [Ashish Tawari](https://dblp.org/pid/59/8617.html), [Mubarak Shah](https://dblp.org/pid/s/MubarakShah.html), [Son Tran](https://dblp.org/pid/19/2438.html), [Raffay Hamid](https://dblp.org/pid/38/51.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html), [Abhinav Shrivastava](https://dblp.org/pid/65/10572.html):

CoLLM: A Large Language Model for Composed Image Retrieval. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/HuynhYTSTHCS25): 3994-4004
- ![](https://dblp.org/img/n.png)

\[c40\]
[Chen Wan](https://dblp.org/pid/293/0656.html), [Teng Jin](https://dblp.org/pid/282/8285.html), Jinyu Yang, [Fangyi Wang](https://dblp.org/pid/163/9017.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Low-visibility Crop Detection in Agricultural Scenes via Point Cloud Guidance. [IJCNN2025](https://dblp.org/db/conf/ijcnn/ijcnn2025.html#conf/ijcnn/WanJYWZ25): 1-10
- ![](https://dblp.org/img/n.png)

\[c39\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Liangwei Yang](https://dblp.org/pid/260/5064.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zeyuan Guo](https://dblp.org/pid/395/4778.html), [Jiayi Gao](https://dblp.org/pid/315/3227.html), [Jing Wu](https://dblp.org/pid/88/3604.html), [Tianhao Chai](https://dblp.org/pid/421/2898.html), [Hai Huang](https://dblp.org/pid/51/944.html), [Cheng Yang](https://dblp.org/pid/49/1457-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chuan Shi](https://dblp.org/pid/64/3041-1.html):

Benchmarking Graph Foundation Models. [KDD (2)2025](https://dblp.org/db/conf/kdd/kdd2025-2.html#conf/kdd/YangYGGWCH0025): 5866-5875
- ![](https://dblp.org/img/n.png)

\[c38\]
[Jiali Chen](https://dblp.org/pid/14/2352.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yujie Jia](https://dblp.org/pid/241/5998.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zihan Wu](https://dblp.org/pid/354/8152.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Jianpeng Chen](https://dblp.org/pid/234/5858.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xusen Hei](https://dblp.org/pid/389/2648.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiayuan Xie](https://dblp.org/pid/249/8382.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Cai](https://dblp.org/pid/58/3467-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Li](https://dblp.org/pid/181/2689-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ExpStar: Towards Automatic Commentary Generation for Multi-discipline Scientific Experiments. [ACM Multimedia2025](https://dblp.org/db/conf/mm/mm2025.html#conf/mm/ChenJWYCHX0025): 6576-6585
- ![](https://dblp.org/img/n.png)

\[i37\]
[Jianzheng Huang](https://dblp.org/pid/402/1445.html), [Xianyu Mo](https://dblp.org/pid/402/0908.html), [Ziling Liu](https://dblp.org/pid/328/8536.html), Jinyu Yang, [Feng Zheng](https://dblp.org/pid/39/800-1.html):

GIFT: Generated Indoor video frames for Texture-less point tracking. [CoRRabs/2503.12944](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-12944) (2025)
- ![](https://dblp.org/img/n.png)

\[i36\]
[Chuong Huynh](https://dblp.org/pid/289/7090.html), Jinyu Yang, [Ashish Tawari](https://dblp.org/pid/59/8617.html), [Mubarak Shah](https://dblp.org/pid/s/MubarakShah.html), [Son Tran](https://dblp.org/pid/19/2438.html), [Raffay Hamid](https://dblp.org/pid/38/51.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html), [Abhinav Shrivastava](https://dblp.org/pid/65/10572.html):

CoLLM: A Large Language Model for Composed Image Retrieval. [CoRRabs/2503.19910](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-19910) (2025)
- ![](https://dblp.org/img/n.png)

\[i35\]
[Yixuan Yang](https://dblp.org/pid/229/1326.html), Jinyu Yang, [Zixiang Zhao](https://dblp.org/pid/65/5420.html), [Victor Sanchez](https://dblp.org/pid/96/2574.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

RefComp: A Reference-guided Unified Framework for Unpaired Point Cloud Completion. [CoRRabs/2504.13788](https://dblp.org/db/journals/corr/corr2504.html#journals/corr/abs-2504-13788) (2025)
- ![](https://dblp.org/img/n.png)

\[i34\]
Jinyu Yang, [Cheng Yang](https://dblp.org/pid/49/1457-2.html), [Shanyuan Cui](https://dblp.org/pid/409/8702.html), [Zeyuan Guo](https://dblp.org/pid/395/4778.html), [Liangwei Yang](https://dblp.org/pid/260/5064.html), [Muhan Zhang](https://dblp.org/pid/157/5518.html), [Chuan Shi](https://dblp.org/pid/64/3041-1.html):

Masked Language Models are Good Heterogeneous Graph Generalizers. [CoRRabs/2506.06157](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-06157) (2025)
- ![](https://dblp.org/img/n.png)

\[i33\]
[Yixuan Yang](https://dblp.org/pid/229/1326.html), [Zhen Luo](https://dblp.org/pid/93/1458.html), [Tongsheng Ding](https://dblp.org/pid/394/9084.html), [Junru Lu](https://dblp.org/pid/194/4596.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), Jinyu Yang, [Victor Sanchez](https://dblp.org/pid/96/2574.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization. [CoRRabs/2506.07570](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-07570) (2025)
- ![](https://dblp.org/img/n.png)

\[i32\]
[Zihao Zhao](https://dblp.org/pid/63/9613.html), [Xinlong Zhai](https://dblp.org/pid/402/0457.html), Jinyu Yang, [Chuan Shi](https://dblp.org/pid/64/3041-1.html):

Towards Text-free Graph Foundation Models: Rethinking Multi-Domain Graph Contrastive Learning. [CoRRabs/2506.22510](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-22510) (2025)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Jiali Chen](https://dblp.org/pid/14/2352.html), [Yujie Jia](https://dblp.org/pid/241/5998.html), [Zihan Wu](https://dblp.org/pid/354/8152.html), Jinyu Yang, [Jianpeng Chen](https://dblp.org/pid/234/5858.html), [Xusen Hei](https://dblp.org/pid/389/2648.html), [Jiayuan Xie](https://dblp.org/pid/249/8382.html), [Yi Cai](https://dblp.org/pid/58/3467-1.html), [Qing Li](https://dblp.org/pid/181/2689-1.html):

ExpStar: Towards Automatic Commentary Generation for Multi-discipline Scientific Experiments. [CoRRabs/2507.09693](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-09693) (2025)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Ziling Liu](https://dblp.org/pid/328/8536.html), [Ziwei Chen](https://dblp.org/pid/219/9605.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), Jinyu Yang, [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Leveraging Geometric Priors for Unaligned Scene Change Detection. [CoRRabs/2509.11292](https://dblp.org/db/journals/corr/corr2509.html#journals/corr/abs-2509-11292) (2025)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Xusen Hei](https://dblp.org/pid/389/2648.html), [Jiali Chen](https://dblp.org/pid/14/2352.html), Jinyu Yang, [Mengchen Zhao](https://dblp.org/pid/178/8719.html), [Yi Cai](https://dblp.org/pid/58/3467-1.html):

ViRectify: A Challenging Benchmark for Video Reasoning Correction with Multimodal Large Language Models. [CoRRabs/2512.01424](https://dblp.org/db/journals/corr/corr2512.html#journals/corr/abs-2512-01424) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j24\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Dongdong Bai](https://dblp.org/pid/196/7870.html), [Xing Yuan](https://dblp.org/pid/221/0150.html), [Dongmei Li](https://dblp.org/pid/27/1131.html):

Anti-Jamming UAV Relaying Based on Joint Geographic-Electromagnetic Domain Optimization. [IEEE Access12](https://dblp.org/db/journals/access/access12.html#journals/access/YangBYL24): 53928-53943 (2024)
- ![](https://dblp.org/img/n.png)

\[j23\]
Jinyu Yang, [Wenqing Zhang](https://dblp.org/pid/138/8580.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiande Zhao](https://dblp.org/pid/76/5803.html)![](https://dblp.org/img/orcid-mark.12x12.png):

How can suppliers strategically involve downstream manufacturers in research and development collaboration? A knowledge spillover perspective. [Eur. J. Oper. Res.314(1)](https://dblp.org/db/journals/eor/eor314.html#journals/eor/YangZZ24): 122-135 (2024)
- ![](https://dblp.org/img/n.png)

\[j22\]
[Shunqi Mei](https://dblp.org/pid/72/4243.html), Jinyu Yang, [Bin Xu](https://dblp.org/pid/69/7024.html), [Jia Chen](https://dblp.org/pid/99/6879.html), [Cong Zhou](https://dblp.org/pid/44/3148.html):

Effect of Heat Treatment on Chemical Plating of Ni-Cr-P on 65Mn Alloy Steel. [Int. J. Inf. Retr. Res.14](https://dblp.org/db/journals/ijirr/ijirr14.html#journals/ijirr/MeiYXCZ24): 1-24 (2024)
- ![](https://dblp.org/img/n.png)

\[j21\]
[Jin Zhang](https://dblp.org/pid/43/6657.html), [Yanjiao Shi](https://dblp.org/pid/154/1947.html), Jinyu Yang, [Qianqian Guo](https://dblp.org/pid/04/9458.html):

KD-SCFNet: Towards more accurate and lightweight salient object detection via knowledge distillation. [Neurocomputing572](https://dblp.org/db/journals/ijon/ijon572.html#journals/ijon/ZhangSYG24): 127206 (2024)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Qianqian Guo](https://dblp.org/pid/04/9458.html), [Yanjiao Shi](https://dblp.org/pid/154/1947.html), [Jin Zhang](https://dblp.org/pid/43/6657.html), Jinyu Yang, [Qing Zhang](https://dblp.org/pid/68/1429-4.html):

D2Net: discriminative feature extraction and details preservation network for salient object detection. [J. Electronic Imaging33(4)](https://dblp.org/db/journals/jei/jei33.html#journals/jei/GuoSZYZ24) (2024)
- ![](https://dblp.org/img/n.png)

\[j19\]
[Chunyan Wang](https://dblp.org/pid/287/5495.html), [Min-Qian Liu](https://dblp.org/pid/28/1560.html), Jinyu Yang:

A New Class of Strong Orthogonal Arrays of Strength Three. [J. Syst. Sci. Complex.37(3)](https://dblp.org/db/journals/jossac/jossac37.html#journals/jossac/WangLY24): 1233-1250 (2024)
- ![](https://dblp.org/img/n.png)

\[j18\]
Jinyu Yang, [Yanjiao Shi](https://dblp.org/pid/154/1947.html), [Jin Zhang](https://dblp.org/pid/43/6657.html), [Qianqian Guo](https://dblp.org/pid/04/9458.html), [Qing Zhang](https://dblp.org/pid/68/1429-4.html), [Liu Cui](https://dblp.org/pid/143/0951.html):

Multi-branch feature fusion and refinement network for salient object detection. [Multim. Syst.30(4)](https://dblp.org/db/journals/mms/mms30.html#journals/mms/YangSZGZC24): 190 (2024)
- ![](https://dblp.org/img/n.png)

\[j17\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Runmin Cong](https://dblp.org/pid/180/7852.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chengjie Wang](https://dblp.org/pid/142/0008-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unveiling the Power of Visible-Thermal Video Object Segmentation. [IEEE Trans. Circuits Syst. Video Technol.34(7)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/Yang0CWZL24): 5376-5388 (2024)
- ![](https://dblp.org/img/n.png)

\[j16\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Qingqing Bi](https://dblp.org/pid/41/10676.html)![](https://dblp.org/img/orcid-mark.12x12.png):

R&D Partner's Network Position and Focal Firm's Innovation Performance: A Knowledge Spill-In Perspective. [IEEE Trans. Engineering Management71](https://dblp.org/db/journals/tem/tem71.html#journals/tem/YangB24): 5982-5997 (2024)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Jiacheng Hou](https://dblp.org/pid/226/4634.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Chengjie Wang](https://dblp.org/pid/142/0008-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

MCD-Net: Toward RGB-D Video Inpainting in Real-World Scenes. [IEEE Trans. Image Process.33](https://dblp.org/db/journals/tip/tip33.html#journals/tip/HouJYWZ24): 1095-1108 (2024)
- ![](https://dblp.org/img/n.png)

\[j14\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiantong Zhen](https://dblp.org/pid/78/10651.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rongrong Ji](https://dblp.org/pid/86/5681.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Weakly-Supervised RGBD Video Object Segmentation. [IEEE Trans. Image Process.33](https://dblp.org/db/journals/tip/tip33.html#journals/tip/YangGZZJSL24): 2158-2170 (2024)
- ![](https://dblp.org/img/n.png)

\[c37\]
[Liqiong Wang](https://dblp.org/pid/311/0165.html), Jinyu Yang, [Yanfu Zhang](https://dblp.org/pid/154/7698.html), [Fangyi Wang](https://dblp.org/pid/163/9017.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Depth-Aware Concealed Crop Detection in Dense Agricultural Scenes. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/WangYZWZ24): 17201-17211
- ![](https://dblp.org/img/n.png)

\[c36\]
[Sirnam Swetha](https://dblp.org/pid/171/5561.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Tal Neiman](https://dblp.org/pid/155/3492.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mamshad Nayeem Rizve](https://dblp.org/pid/260/4900.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Son Tran](https://dblp.org/pid/19/2438.html), [Benjamin Z. Yao](https://dblp.org/pid/134/7162.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html), [Mubarak Shah](https://dblp.org/pid/s/MubarakShah.html):

X-Former: Unifying Contrastive and Reconstruction Learning for MLLMs. [ECCV (6)2024](https://dblp.org/db/conf/eccv/eccv2024-6.html#conf/eccv/SwethaYNRTYCS24): 146-162
- ![](https://dblp.org/img/n.png)

\[c35\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Pavel Tokmakov](https://dblp.org/pid/153/2264.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Khanh-Tung Tran](https://dblp.org/pid/359/3793.html), [Xuan-Son Vu](https://dblp.org/pid/151/8673.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Minasadat Attari](https://dblp.org/pid/370/3618.html), [Antoni B. Chan](https://dblp.org/pid/55/5814.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liang Chen](https://dblp.org/pid/01/5394.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Jaired Collins](https://dblp.org/pid/211/4242.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Ganesh Sai Manas Devarapu](https://dblp.org/pid/406/4906.html), [Yinglong Du](https://dblp.org/pid/199/1274.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Wan-Cyuan Fan](https://dblp.org/pid/300/5836.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Raghav Goyal](https://dblp.org/pid/191/6034.html), [Jungong Han](https://dblp.org/pid/98/6127.html), [Bijaya Kumar Hatuwal](https://dblp.org/pid/318/9407.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Xiantao Hu](https://dblp.org/pid/160/8016.html), [Xingsen Huang](https://dblp.org/pid/284/1333.html), [Yuqing Huang](https://dblp.org/pid/134/5853.html), [Dongmei Jiang](https://dblp.org/pid/47/1926.html), [Ben Kang](https://dblp.org/pid/340/1671.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Ning Li](https://dblp.org/pid/14/5410-44.html), [Xiaohai Li](https://dblp.org/pid/00/38.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Cheng Liang](https://dblp.org/pid/81/9078.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Ting Liu](https://dblp.org/pid/52/5150-18.html), [Ziquan Liu](https://dblp.org/pid/207/9035.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Yifei Luo](https://dblp.org/pid/58/3045.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Juan David Mogollon](https://dblp.org/pid/325/7624.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ziqi Pang](https://dblp.org/pid/255/9210.html), [Jaswanth Reddy Pochimireddy](https://dblp.org/pid/406/5059.html), [Viktor Prutyanov](https://dblp.org/pid/245/3321.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gani Rahmon](https://dblp.org/pid/291/7224.html), [Aleksandr Romanov](https://dblp.org/pid/239/5991.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liangtao Shi](https://dblp.org/pid/366/5426.html), [Mennatullah Siam](https://dblp.org/pid/163/9048.html), [Leonid Sigal](https://dblp.org/pid/09/4991.html), [Arun Kumar Sivapuram](https://dblp.org/pid/344/4532.html), [Roman A. Solovyev](https://dblp.org/pid/163/3390.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Elham Soltani Kazemi](https://dblp.org/pid/318/1851.html), [Imad Eddine Toubal](https://dblp.org/pid/292/6360.html), [Jia Wan](https://dblp.org/pid/13/6504-1.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Xinying Wang](https://dblp.org/pid/06/3244-5.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Yu-Xiong Wang](https://dblp.org/pid/35/10700.html), [Zhiquan Wang](https://dblp.org/pid/18/5129.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Qiangqiang Wu](https://dblp.org/pid/193/1415.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Zihao Xia](https://dblp.org/pid/382/4580.html), [Jinxia Xie](https://dblp.org/pid/294/3376.html), [Chenlong Xu](https://dblp.org/pid/315/8714.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Chaocan Xue](https://dblp.org/pid/334/6591.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chao Yang](https://dblp.org/pid/00/5867.html), Jinyu Yang, [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Chenyang Yu](https://dblp.org/pid/287/4163.html), [Ke Yu](https://dblp.org/pid/23/2089.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiaming Zhang](https://dblp.org/pid/81/10010-6.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Yaozong Zheng](https://dblp.org/pid/344/6907.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jinglin Zhou](https://dblp.org/pid/48/6808.html), [Junbao Zhou](https://dblp.org/pid/340/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yong Zhou](https://dblp.org/pid/90/5836.html), [Zikun Zhou](https://dblp.org/pid/271/8084.html), [Guibo Zhu](https://dblp.org/pid/125/2113.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Vladimir V. Zunin](https://dblp.org/pid/372/7918.html)![](https://dblp.org/img/orcid-mark.12x12.png):

The Second Visual Object Tracking Segmentation VOTS2024 Challenge Results. [ECCV Workshops (7)2024](https://dblp.org/db/conf/eccv/eccv2024-w7.html#conf/eccv/KristanMTFZLTVBCFACCCCC24): 357-383
- ![](https://dblp.org/img/n.png)

\[c34\]
[Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chang Liu](https://dblp.org/pid/52/5716-72.html), [Yunchao Wei](https://dblp.org/pid/118/5394.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nikhila Ravi](https://dblp.org/pid/248/7650.html), [Shuting He](https://dblp.org/pid/255/9456.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Bai](https://dblp.org/pid/151/6422-1.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Zhensong Xu](https://dblp.org/pid/149/5188.html), [Jiangtao Yao](https://dblp.org/pid/294/5962.html), [Chengjing Wu](https://dblp.org/pid/379/5986.html), [Ting Liu](https://dblp.org/pid/52/5150-18.html), [Luoqi Liu](https://dblp.org/pid/29/8842.html), [Xinyu Liu](https://dblp.org/pid/98/738.html), [Jing Zhang](https://dblp.org/pid/05/3499-37.html), [Kexin Zhang](https://dblp.org/pid/119/0668-3.html), [Yuting Yang](https://dblp.org/pid/25/3635-8.html), [Licheng Jiao](https://dblp.org/pid/40/3714.html), [Shuyuan Yang](https://dblp.org/pid/81/2383.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingnan Luo](https://dblp.org/pid/379/6720.html), Jinyu Yang, [Jungong Han](https://dblp.org/pid/98/6127.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Bin Cao](https://dblp.org/pid/17/1169.html), [Yisi Zhang](https://dblp.org/pid/318/0710.html), [Xuanxu Lin](https://dblp.org/pid/380/2324.html), [Xingjian He](https://dblp.org/pid/204/0216.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html), [Jing Liu](https://dblp.org/pid/72/2590-1.html), [Feiyu Pan](https://dblp.org/pid/142/1276.html), [Hao Fang](https://dblp.org/pid/06/2484-10.html), [Xiankai Lu](https://dblp.org/pid/153/2122.html):

PVUW 2024 Challenge on Complex Video Understanding: Methods and Results. [ECCV Workshops (10)2024](https://dblp.org/db/conf/eccv/eccv2024-w10.html#conf/eccv/DingLWRHBTMLHWYXYWLLLZZ24): 361-377
- ![](https://dblp.org/img/n.png)

\[c33\]
[Lu Li](https://dblp.org/pid/72/2266.html), [Yanjiao Shi](https://dblp.org/pid/154/1947.html), Jinyu Yang, [Qiangqiang Zhou](https://dblp.org/pid/161/2504.html), [Qing Zhang](https://dblp.org/pid/68/1429.html), [Liu Cui](https://dblp.org/pid/143/0951.html):

Transformer-Based Depth Optimization Network for RGB-D Salient Object Detection. [ICPR (21)2024](https://dblp.org/db/conf/icpr/icpr2024-21.html#conf/icpr/LiSYZZC24): 435-450
- ![](https://dblp.org/img/n.png)

\[c32\]
[Ziling Liu](https://dblp.org/pid/328/8536.html), Jinyu Yang, [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Place Anything into Any Video. [IJCAI2024](https://dblp.org/db/conf/ijcai/ijcai2024.html#conf/ijcai/LiuY0Z24): 8729-8732
- ![](https://dblp.org/img/n.png)

\[c31\]
[Robin Jeanne Kirschner](https://dblp.org/pid/292/8686.html), Jinyu Yang, [Edonis Elshani](https://dblp.org/pid/385/2924.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Carina M. Micheler](https://dblp.org/pid/327/5319.html), [Tobias Leibbrand](https://dblp.org/pid/385/3344.html), [Dirk Müller](https://dblp.org/pid/58/1717.html), [Claudio Glowalla](https://dblp.org/pid/303/2970.html), [Nader Rajaei](https://dblp.org/pid/227/8455.html), [Rainer Burgkart](https://dblp.org/pid/40/5566.html), [Sami Haddadin](https://dblp.org/pid/01/3198.html):

Towards Unconstrained Collision Injury Protection Data Sets: Initial Surrogate Experiments for the Human Hand. [IROS2024](https://dblp.org/db/conf/iros/iros2024.html#conf/iros/KirschnerYEMLMG24): 14012-14019
- ![](https://dblp.org/img/n.png)

\[c30\]
[Xinliang Zhu](https://dblp.org/pid/160/9968.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sheng-Wei Huang](https://dblp.org/pid/67/6807.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Han Ding](https://dblp.org/pid/88/886-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Kelvin Chen](https://dblp.org/pid/187/0349.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tao Zhou](https://dblp.org/pid/98/4450.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tal Neiman](https://dblp.org/pid/155/3492.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ouye Xie](https://dblp.org/pid/382/3920.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Son Tran](https://dblp.org/pid/19/2438.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Benjamin Z. Yao](https://dblp.org/pid/134/7162.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Douglas Gray](https://dblp.org/pid/78/2781.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Anuj Bindal](https://dblp.org/pid/383/9891.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Arnab Dhua](https://dblp.org/pid/96/2760.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Bringing Multimodality to Amazon Visual Search System. [KDD2024](https://dblp.org/db/conf/kdd/kdd2024.html#conf/kdd/ZhuH0YCZNXTY0BD24): 6390-6399
- ![](https://dblp.org/img/n.png)

\[i28\]
Jinyu Yang, [Camille Vindolet](https://dblp.org/pid/341/9857.html), [Julio Rogelio Guadarrama-Olvera](https://dblp.org/pid/141/7418.html), [Gordon Cheng](https://dblp.org/pid/03/2800.html):

On the impact of robot personalization on human-robot interaction: A review. [CoRRabs/2401.11776](https://dblp.org/db/journals/corr/corr2401.html#journals/corr/abs-2401-11776) (2024)
- ![](https://dblp.org/img/n.png)

\[i27\]
[Ziling Liu](https://dblp.org/pid/328/8536.html), Jinyu Yang, [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Place Anything into Any Video. [CoRRabs/2402.14316](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-14316) (2024)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingnan Luo](https://dblp.org/pid/379/6720.html), Jinyu Yang, [Jungong Han](https://dblp.org/pid/98/6127.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

1st Place Solution for MeViS Track in CVPR 2024 PVUW Workshop: Motion Expression guided Video Segmentation. [CoRRabs/2406.07043](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-07043) (2024)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Henghui Ding](https://dblp.org/pid/230/1216.html), [Chang Liu](https://dblp.org/pid/52/5716-72.html), [Yunchao Wei](https://dblp.org/pid/118/5394.html), [Nikhila Ravi](https://dblp.org/pid/248/7650.html), [Shuting He](https://dblp.org/pid/255/9456.html), [Song Bai](https://dblp.org/pid/151/6422-1.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Zhensong Xu](https://dblp.org/pid/149/5188.html), [Jiangtao Yao](https://dblp.org/pid/294/5962.html), [Chengjing Wu](https://dblp.org/pid/379/5986.html), [Ting Liu](https://dblp.org/pid/52/5150-18.html), [Luoqi Liu](https://dblp.org/pid/29/8842.html), [Xinyu Liu](https://dblp.org/pid/98/738.html), [Jing Zhang](https://dblp.org/pid/05/3499-37.html), [Kexin Zhang](https://dblp.org/pid/119/0668-3.html), [Yuting Yang](https://dblp.org/pid/25/3635-8.html), [Licheng Jiao](https://dblp.org/pid/40/3714.html), [Shuyuan Yang](https://dblp.org/pid/81/2383.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingnan Luo](https://dblp.org/pid/379/6720.html), Jinyu Yang, [Jungong Han](https://dblp.org/pid/98/6127.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Bin Cao](https://dblp.org/pid/17/1169.html), [Yisi Zhang](https://dblp.org/pid/318/0710.html), [Xuanxu Lin](https://dblp.org/pid/380/2324.html), [Xingjian He](https://dblp.org/pid/204/0216.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html), [Jing Liu](https://dblp.org/pid/72/2590-1.html), [Feiyu Pan](https://dblp.org/pid/142/1276.html), [Hao Fang](https://dblp.org/pid/06/2484-10.html), [Xiankai Lu](https://dblp.org/pid/153/2122.html):

PVUW 2024 Challenge on Complex Video Understanding: Methods and Results. [CoRRabs/2406.17005](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-17005) (2024)
- ![](https://dblp.org/img/n.png)

\[i24\]
[Sirnam Swetha](https://dblp.org/pid/171/5561.html), Jinyu Yang, [Tal Neiman](https://dblp.org/pid/155/3492.html), [Mamshad Nayeem Rizve](https://dblp.org/pid/260/4900.html), [Son Tran](https://dblp.org/pid/19/2438.html), [Benjamin Z. Yao](https://dblp.org/pid/134/7162.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html), [Mubarak Shah](https://dblp.org/pid/s/MubarakShah.html):

X-Former: Unifying Contrastive and Reconstruction Learning for MLLMs. [CoRRabs/2407.13851](https://dblp.org/db/journals/corr/corr2407.html#journals/corr/abs-2407-13851) (2024)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Robin Jeanne Kirschner](https://dblp.org/pid/292/8686.html), Jinyu Yang, [Edonis Elshani](https://dblp.org/pid/385/2924.html), [Carina M. Micheler](https://dblp.org/pid/327/5319.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tobias Leibbrand](https://dblp.org/pid/385/3344.html), [Dirk Müller](https://dblp.org/pid/58/1717.html), [Claudio Glowalla](https://dblp.org/pid/303/2970.html), [Nader Rajaei](https://dblp.org/pid/227/8455.html), [Rainer Burgkart](https://dblp.org/pid/40/5566.html), [Sami Haddadin](https://dblp.org/pid/01/3198.html):

Towards Unconstrained Collision Injury Protection Data Sets: Initial Surrogate Experiments for the Human Hand. [CoRRabs/2408.06175](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-06175) (2024)
- ![](https://dblp.org/img/n.png)

\[i22\]
Jinyu Yang, [Qingwei Wang](https://dblp.org/pid/88/2321.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Peng Chen](https://dblp.org/pid/27/7017.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Deng-Ping Fan](https://dblp.org/pid/205/3148.html):

PlantCamo: Plant Camouflage Detection. [CoRRabs/2410.17598](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-17598) (2024)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Liqiong Wang](https://dblp.org/pid/311/0165.html), [Teng Jin](https://dblp.org/pid/282/8285.html), Jinyu Yang, [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Fangyi Wang](https://dblp.org/pid/163/9017.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Agri-LLaVA: Knowledge-Infused Large Multimodal Assistant on Agricultural Pests and Diseases. [CoRRabs/2412.02158](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-02158) (2024)
- ![](https://dblp.org/img/n.png)

\[i20\]
[Xinliang Zhu](https://dblp.org/pid/160/9968.html), [Michael Huang](https://dblp.org/pid/87/6759.html), [Han Ding](https://dblp.org/pid/88/886-4.html), Jinyu Yang, [Kelvin Chen](https://dblp.org/pid/187/0349.html), [Tao Zhou](https://dblp.org/pid/98/4450.html), [Tal Neiman](https://dblp.org/pid/155/3492.html), [Ouye Xie](https://dblp.org/pid/382/3920.html), [Son Tran](https://dblp.org/pid/19/2438.html), [Benjamin Z. Yao](https://dblp.org/pid/134/7162.html), [Douglas Gray](https://dblp.org/pid/78/2781.html), [Anuj Bindal](https://dblp.org/pid/383/9891.html), [Arnab Dhua](https://dblp.org/pid/96/2760.html):

Bringing Multimodality to Amazon Visual Search System. [CoRRabs/2412.13364](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-13364) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j13\]
[Chaochao Yan](https://dblp.org/pid/223/4751.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang, [Hehuan Ma](https://dblp.org/pid/263/2003.html), [Sheng Wang](https://dblp.org/pid/85/1868-1.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Molecule Sequence Generation with Rebalanced Variational Autoencoder Loss. [J. Comput. Biol.30(1)](https://dblp.org/db/journals/jcb/jcb30.html#journals/jcb/YanYMWH23): 82-94 (2023)
- ![](https://dblp.org/img/n.png)

\[j12\]
[Xiaole Jia](https://dblp.org/pid/358/3210.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yibo Wang](https://dblp.org/pid/25/4764.html), Jinyu Yang, [Yan Liu](https://dblp.org/pid/150/4295.html), [Yue Hao](https://dblp.org/pid/17/1995-1.html), [Genquan Han](https://dblp.org/pid/269/2129.html):

A compact model of DC _I_- _V_ characteristics for depleted Ga2O3 MOSFETs. [Microelectron. J.140](https://dblp.org/db/journals/mj/mj140.html#journals/mj/JiaWYLHH23): 105920 (2023)
- ![](https://dblp.org/img/n.png)

\[j11\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang, [Jungong Han](https://dblp.org/pid/98/6127.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ke Lu](https://dblp.org/pid/33/1254-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Giovanni Montana](https://dblp.org/pid/89/449.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Decoupling Multimodal Transformers for Referring Video Object Segmentation. [IEEE Trans. Circuits Syst. Video Technol.33(9)](https://dblp.org/db/journals/tcsv/tcsv33.html#journals/tcsv/GaoYHLZM23): 4518-4528 (2023)
- ![](https://dblp.org/img/n.png)

\[c29\]
[Peiyang Liu](https://dblp.org/pid/275/7551.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Lin Wang](https://dblp.org/pid/17/6729-106.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sen Wang](https://dblp.org/pid/69/6403.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlai Hao](https://dblp.org/pid/358/7797.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huihui Bai](https://dblp.org/pid/75/5070-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Retrieval-Based Unsupervised Noisy Label Detection on Text Data. [CIKM2023](https://dblp.org/db/conf/cikm/cikm2023.html#conf/cikm/LiuYWWHB23): 4099-4104
- ![](https://dblp.org/img/n.png)

\[c28\]
[Kushal Kumar](https://dblp.org/pid/318/2740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tarik Arici](https://dblp.org/pid/14/5731.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tal Neiman](https://dblp.org/pid/155/3492.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Shioulin Sam](https://dblp.org/pid/358/8004.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Xu](https://dblp.org/pid/14/5580-11.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hakan Ferhatosmanoglu](https://dblp.org/pid/f/HFerhatosmanoglu.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ismail B. Tutar](https://dblp.org/pid/17/5973.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unsupervised Multi-Modal Representation Learning for High Quality Retrieval of Similar Products at E-commerce Scale. [CIKM2023](https://dblp.org/db/conf/cikm/cikm2023.html#conf/cikm/KumarANYSXFT23): 4667-4673
- ![](https://dblp.org/img/n.png)

\[c27\]
[Yijian Liu](https://dblp.org/pid/40/6142.html), [Hongyi Zhang](https://dblp.org/pid/28/4536.html), [Cheng Yang](https://dblp.org/pid/49/1457-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ao Li](https://dblp.org/pid/54/2788.html), [Yugang Ji](https://dblp.org/pid/184/0823.html), [Luhao Zhang](https://dblp.org/pid/254/8164.html), [Tao Li](https://dblp.org/pid/75/4601.html), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Tianyu Zhao](https://dblp.org/pid/139/3492.html), [Juan Yang](https://dblp.org/pid/22/815.html), [Hai Huang](https://dblp.org/pid/51/944.html), [Chuan Shi](https://dblp.org/pid/64/3041-1.html):

Datasets and Interfaces for Benchmarking Heterogeneous Graph Neural Networks. [CIKM2023](https://dblp.org/db/conf/cikm/cikm2023.html#conf/cikm/LiuZYLJZLYZYHS23): 5346-5350
- ![](https://dblp.org/img/n.png)

\[c26\]
Jinyu Yang, [Shang Gao](https://dblp.org/pid/28/435-12.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html):

Resource-Efficient RGBD Aerial Tracking. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/YangGLZL23): 13374-13383
- ![](https://dblp.org/img/n.png)

\[c25\]
[Qingwei Wang](https://dblp.org/pid/88/2321.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaosheng Yu](https://dblp.org/pid/99/8589-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fangyi Wang](https://dblp.org/pid/163/9017.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peng Chen](https://dblp.org/pid/27/7017.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Depth-aided Camouflaged Object Detection. [ACM Multimedia2023](https://dblp.org/db/conf/mm/mm2023.html#conf/mm/WangYYWCZ23): 3297-3306
- ![](https://dblp.org/img/n.png)

\[c24\]
Jinyu Yang, [Jingjing Liu](https://dblp.org/pid/30/3008.html), [Ning Xu](https://dblp.org/pid/04/5856.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

TVT: Transferable Vision Transformer for Unsupervised Domain Adaptation. [WACV2023](https://dblp.org/db/conf/wacv/wacv2023.html#conf/wacv/YangLXH23): 520-530
- ![](https://dblp.org/img/n.png)

\[i19\]
Jinyu Yang, [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Fangjing Wang](https://dblp.org/pid/249/7437.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Track Anything: Segment Anything Meets Videos. [CoRRabs/2304.11968](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-11968) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j10\]
[Jin Zhang](https://dblp.org/pid/43/6657.html), [Qiuwei Liang](https://dblp.org/pid/318/8564.html), [Qianqian Guo](https://dblp.org/pid/04/9458.html), Jinyu Yang, [Qing Zhang](https://dblp.org/pid/68/1429-4.html), [Yanjiao Shi](https://dblp.org/pid/154/1947.html):

R2Net: Residual refinement network for salient object detection. [Image Vis. Comput.120](https://dblp.org/db/journals/ivc/ivc120.html#journals/ivc/ZhangLGYZS22): 104423 (2022)
- ![](https://dblp.org/img/n.png)

\[c23\]
[Weizhi An](https://dblp.org/pid/224/2525.html), [Yuzhi Guo](https://dblp.org/pid/249/0479.html), [Yatao Bian](https://dblp.org/pid/222/2694.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hehuan Ma](https://dblp.org/pid/263/2003.html), Jinyu Yang, [Chunyuan Li](https://dblp.org/pid/64/9590.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

MoDNA: motif-oriented pre-training for DNA language model. [BCB2022](https://dblp.org/db/conf/bcb/bcb2022.html#conf/bcb/AnGBMYLH22): 5:1-5:5
- ![](https://dblp.org/img/n.png)

\[c22\]
[Jiali Duan](https://dblp.org/pid/187/1570.html), [Liqun Chen](https://dblp.org/pid/22/150-1.html), [Son Tran](https://dblp.org/pid/19/2438.html), Jinyu Yang, [Yi Xu](https://dblp.org/pid/14/5580-11.html), [Belinda Zeng](https://dblp.org/pid/277/3956.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html):

Multi-modal Alignment using Representation Codebook. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/DuanCTYXZC22): 15630-15639
- ![](https://dblp.org/img/n.png)

\[c21\]
Jinyu Yang, [Jiali Duan](https://dblp.org/pid/187/1570.html), [Son Tran](https://dblp.org/pid/19/2438.html), [Yi Xu](https://dblp.org/pid/14/5580-11.html), [Sampath Chanda](https://dblp.org/pid/244/2140.html), [Liqun Chen](https://dblp.org/pid/22/150-1.html), [Belinda Zeng](https://dblp.org/pid/277/3956.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Vision-Language Pre-Training with Triple Contrastive Learning. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/YangDTXCCZCH22): 15650-15659
- ![](https://dblp.org/img/n.png)

\[c20\]
Jinyu Yang, [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html):

Towards Generic 3D Tracking in RGBD Videos: Benchmark and Baseline. [ECCV (22)2022](https://dblp.org/db/conf/eccv/eccv2022-22.html#conf/eccv/YangZLCLZ22): 112-128
- ![](https://dblp.org/img/n.png)

\[c19\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), Jinyu Yang, [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- ![](https://dblp.org/img/n.png)

\[c18\]
[Shang Gao](https://dblp.org/pid/28/435-12.html), Jinyu Yang, [Zhe Li](https://dblp.org/pid/11/751-8.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jingkuan Song](https://dblp.org/pid/70/10575.html):

Learning Dual-Fused Modality-Aware Representations for RGBD Tracking. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/GaoYLZLS22): 478-494
- ![](https://dblp.org/img/n.png)

\[c17\]
[Paolo Mengoni](https://dblp.org/pid/147/6967.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Empowering COVID-19 Fact-Checking with Extended Knowledge Graphs. [ICCSA (Workshops 1)2022](https://dblp.org/db/conf/iccsa/iccsa2022-w1.html#conf/iccsa/MengoniY22): 138-150
- ![](https://dblp.org/img/n.png)

\[c16\]
Jinyu Yang, [Zhe Li](https://dblp.org/pid/11/751-8.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jingkuan Song](https://dblp.org/pid/70/10575.html):

Prompting for Multi-Modal Tracking. [ACM Multimedia2022](https://dblp.org/db/conf/mm/mm2022.html#conf/mm/YangLZLS22): 3492-3500
- ![](https://dblp.org/img/n.png)

\[i18\]
Jinyu Yang, [Jiali Duan](https://dblp.org/pid/187/1570.html), [Son Tran](https://dblp.org/pid/19/2438.html), [Yi Xu](https://dblp.org/pid/14/5580-11.html), [Sampath Chanda](https://dblp.org/pid/244/2140.html), [Liqun Chen](https://dblp.org/pid/22/150-1.html), [Belinda Zeng](https://dblp.org/pid/277/3956.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

Vision-Language Pre-Training with Triple Contrastive Learning. [CoRRabs/2202.10401](https://dblp.org/db/journals/corr/corr2202.html#journals/corr/abs-2202-10401) (2022)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Jiali Duan](https://dblp.org/pid/187/1570.html), [Liqun Chen](https://dblp.org/pid/22/150-1.html), [Son Tran](https://dblp.org/pid/19/2438.html), Jinyu Yang, [Yi Xu](https://dblp.org/pid/14/5580-11.html), [Belinda Zeng](https://dblp.org/pid/277/3956.html), [Trishul Chilimbi](https://dblp.org/pid/265/6085.html):

Multi-modal Alignment using Representation Codebook. [CoRRabs/2203.00048](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-00048) (2022)
- ![](https://dblp.org/img/n.png)

\[i16\]
Jinyu Yang, [Zhe Li](https://dblp.org/pid/11/751-8.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Ling Shao](https://dblp.org/pid/75/1281.html):

RGBD Object Tracking: An In-depth Review. [CoRRabs/2203.14134](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-14134) (2022)
- ![](https://dblp.org/img/n.png)

\[i15\]
Jinyu Yang, [Zhe Li](https://dblp.org/pid/11/751-8.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jingkuan Song](https://dblp.org/pid/70/10575.html):

Prompting for Multi-Modal Tracking. [CoRRabs/2207.14571](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-14571) (2022)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Shang Gao](https://dblp.org/pid/28/435-12.html), Jinyu Yang, [Zhe Li](https://dblp.org/pid/11/751-8.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jingkuan Song](https://dblp.org/pid/70/10575.html):

Learning Dual-Fused Modality-Aware Representations for RGBD Tracking. [CoRRabs/2211.03055](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-03055) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c15\]
Jinyu Yang, [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Yu Rong](https://dblp.org/pid/24/10036-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chaochao Yan](https://dblp.org/pid/223/4751.html), [Chunyuan Li](https://dblp.org/pid/64/9590.html), [Hehuan Ma](https://dblp.org/pid/263/2003.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

Hierarchical Graph Capsule Network. [AAAI2021](https://dblp.org/db/conf/aaai/aaai2021.html#conf/aaai/YangZRYLMH21): 10603-10611
- ![](https://dblp.org/img/n.png)

\[c14\]
[Song Yan](https://dblp.org/pid/58/6692.html), Jinyu Yang, [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Joni-Kristian Kamarainen](https://dblp.org/pid/k/JoniKristianKamarainen.html):

Depth-only Object Tracking. [BMVC2021](https://dblp.org/db/conf/bmvc/bmvc2021.html#conf/bmvc/YanYLK21): Article 243
- ![](https://dblp.org/img/n.png)

\[c13\]
Jinyu Yang, [Chunyuan Li](https://dblp.org/pid/64/9590.html), [Weizhi An](https://dblp.org/pid/224/2525.html), [Hehuan Ma](https://dblp.org/pid/263/2003.html), [Yuzhi Guo](https://dblp.org/pid/249/0479.html), [Yu Rong](https://dblp.org/pid/24/10036-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Exploring Robustness of Unsupervised Domain Adaptation in Semantic Segmentation. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/YangLAMGRZH21): 9174-9183
- ![](https://dblp.org/img/n.png)

\[c12\]
[Song Yan](https://dblp.org/pid/58/6692.html), Jinyu Yang, [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DepthTrack: Unveiling the Power of RGBD Tracking. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/YanYKZLK21): 10705-10713
- ![](https://dblp.org/img/n.png)

\[c11\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), Jinyu Yang, [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[c10\]
Jinyu Yang, [Weizhi An](https://dblp.org/pid/224/2525.html), [Chaochao Yan](https://dblp.org/pid/223/4751.html), [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Context-Aware Domain Adaptation in Semantic Segmentation. [WACV2021](https://dblp.org/db/conf/wacv/wacv2021.html#conf/wacv/YangAYZH21): 514-524
- ![](https://dblp.org/img/n.png)

\[i13\]
Jinyu Yang, [Chunyuan Li](https://dblp.org/pid/64/9590.html), [Weizhi An](https://dblp.org/pid/224/2525.html), [Hehuan Ma](https://dblp.org/pid/263/2003.html), [Yuzhi Guo](https://dblp.org/pid/249/0479.html), [Yu Rong](https://dblp.org/pid/24/10036-1.html), [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

Exploring Robustness of Unsupervised Domain Adaptation in Semantic Segmentation. [CoRRabs/2105.10843](https://dblp.org/db/journals/corr/corr2105.html#journals/corr/abs-2105-10843) (2021)
- ![](https://dblp.org/img/n.png)

\[i12\]
Jinyu Yang, [Jingjing Liu](https://dblp.org/pid/30/3008.html), [Ning Xu](https://dblp.org/pid/04/5856.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

TVT: Transferable Vision Transformer for Unsupervised Domain Adaptation. [CoRRabs/2108.05988](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-05988) (2021)
- ![](https://dblp.org/img/n.png)

\[i11\]
[Song Yan](https://dblp.org/pid/58/6692.html), Jinyu Yang, [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html):

DepthTrack : Unveiling the Power of RGBD Tracking. [CoRRabs/2108.13962](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-13962) (2021)
- ![](https://dblp.org/img/n.png)

\[i10\]
[Song Yan](https://dblp.org/pid/58/6692.html), Jinyu Yang, [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Joni-Kristian Kamarainen](https://dblp.org/pid/k/JoniKristianKamarainen.html):

Depth-only Object Tracking. [CoRRabs/2110.11679](https://dblp.org/db/journals/corr/corr2110.html#journals/corr/abs-2110-11679) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j9\]
Jinyu Yang, [Hong Peng](https://dblp.org/pid/27/1817-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaohui Luo](https://dblp.org/pid/121/5533.html), [Jun Wang](https://dblp.org/pid/w/JunWang13.html):

Stochastic Numerical P Systems With Application in Data Clustering Problems. [IEEE Access8](https://dblp.org/db/journals/access/access8.html#journals/access/YangPLW20): 31507-31518 (2020)
- ![](https://dblp.org/img/n.png)

\[j8\]
[Chunlei Liu](https://dblp.org/pid/76/5853-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenrui Ding](https://dblp.org/pid/08/10143.html), Jinyu Yang, [Vittorio Murino](https://dblp.org/pid/62/6790.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jungong Han](https://dblp.org/pid/98/6127.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guodong Guo](https://dblp.org/pid/92/4520.html):

Aggregation Signature for Small Object Tracking. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/LiuDYMZHG20): 1738-1747 (2020)
- ![](https://dblp.org/img/n.png)

\[c9\]
[Chaochao Yan](https://dblp.org/pid/223/4751.html), [Sheng Wang](https://dblp.org/pid/85/1868-1.html), Jinyu Yang, [Tingyang Xu](https://dblp.org/pid/157/0940.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Re-balancing Variational Autoencoder Loss for Molecule Sequence Generation. [BCB2020](https://dblp.org/db/conf/bcb/bcb2020.html#conf/bcb/YanWYXH20): 54:1-54:7
- ![](https://dblp.org/img/n.png)

\[c8\]
[Yuzhi Guo](https://dblp.org/pid/249/0479.html), [Jiaxiang Wu](https://dblp.org/pid/119/6799-1.html), [Hehuan Ma](https://dblp.org/pid/263/2003.html), Jinyu Yang, [Xinliang Zhu](https://dblp.org/pid/160/9968.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

WeightAln: Weighted Homologous Alignment for Protein Structure Property Prediction. [BIBM2020](https://dblp.org/db/conf/bibm/bibm2020.html#conf/bibm/GuoWMYZH20): 72-75
- ![](https://dblp.org/img/n.png)

\[c7\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Weizhi An](https://dblp.org/pid/224/2525.html), [Sheng Wang](https://dblp.org/pid/85/1868-1.html), [Xinliang Zhu](https://dblp.org/pid/160/9968.html), [Chaochao Yan](https://dblp.org/pid/223/4751.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Label-Driven Reconstruction for Domain Adaptation in Semantic Segmentation. [ECCV (27)2020](https://dblp.org/db/conf/eccv/eccv2020-27.html#conf/eccv/YangAWZYH20): 480-498
- ![](https://dblp.org/img/n.png)

\[c6\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Linbo He](https://dblp.org/pid/26/741.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Song Yan](https://dblp.org/pid/58/6692.html), Jinyu Yang, [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Alexander G. Hauptmann](https://dblp.org/pid/h/AlexanderGHauptmann.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html), [Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Bing Li](https://dblp.org/pid/13/2692-1.html), [Chen Qian](https://dblp.org/pid/70/3604-6.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Fredrik Gustafsson](https://dblp.org/pid/394/4497.html), [Gian Luca Foresti](https://dblp.org/pid/93/5522.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Haojie Zhao](https://dblp.org/pid/216/7590.html), [Haoran Bai](https://dblp.org/pid/235/9510.html), [Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html), [Houqiang Li](https://dblp.org/pid/59/7017.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Javad Khaghani](https://dblp.org/pid/233/0334.html), [Jesús Bescós](https://dblp.org/pid/97/2333.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Jingtao Xu](https://dblp.org/pid/119/1746.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Junhyun Lee](https://dblp.org/pid/155/8661.html), [Kaicheng Yu](https://dblp.org/pid/198/0861.html), [Kaiwen Liu](https://dblp.org/pid/231/4262.html), [Kang Yang](https://dblp.org/pid/86/8501.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Li Cheng](https://dblp.org/pid/13/4938-1.html), [Li Zhang](https://dblp.org/pid/89/5992-40.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Ning Wang](https://dblp.org/pid/46/2005-20.html), [Pengyu Zhang](https://dblp.org/pid/33/4816.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rama Krishna Sai Subrahmanyam Gorthi](https://dblp.org/pid/45/7595.html), [Seokeon Choi](https://dblp.org/pid/214/2200.html), [Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Shohreh Kasaei](https://dblp.org/pid/78/5062.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Shuhao Chen](https://dblp.org/pid/43/2127.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wengang Zhou](https://dblp.org/pid/22/4544-1.html), [Xi Qiu](https://dblp.org/pid/115/5698.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Xiao-Jun Wu](https://dblp.org/pid/13/5168-1.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Yingming Wang](https://dblp.org/pid/59/605.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuncon Yao](https://dblp.org/pid/284/2556.html), [Yunsung Lee](https://dblp.org/pid/227/9311.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Zezhou Wang](https://dblp.org/pid/204/1179.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhijun Mai](https://dblp.org/pid/247/9401.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Zhirong Wu](https://dblp.org/pid/147/5025.html), [Ziang Ma](https://dblp.org/pid/165/9621.html):

The Eighth Visual Object Tracking VOT2020 Challenge Results. [ECCV Workshops (5)2020](https://dblp.org/db/conf/eccv/eccv2020-w5.html#conf/eccv/KristanLMFPKDZL20): 547-601
- ![](https://dblp.org/img/n.png)

\[c5\]
[Chaochao Yan](https://dblp.org/pid/223/4751.html), [Qianggang Ding](https://dblp.org/pid/247/1295.html), [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Shuangjia Zheng](https://dblp.org/pid/235/3743.html), Jinyu Yang, [Yang Yu](https://dblp.org/pid/46/2181-10.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

RetroXpert: Decompose Retrosynthesis Prediction Like A Chemist. [NeurIPS2020](https://dblp.org/db/conf/nips/neurips2020.html#conf/nips/YanDZZY0H20)
- ![](https://dblp.org/img/n.png)

\[i9\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Weizhi An](https://dblp.org/pid/224/2525.html), [Chaochao Yan](https://dblp.org/pid/223/4751.html), [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

Context-Aware Domain Adaptation in Semantic Segmentation. [CoRRabs/2003.04010](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-04010) (2020)
- ![](https://dblp.org/img/n.png)

\[i8\]
Jinyu Yang, [Weizhi An](https://dblp.org/pid/224/2525.html), [Sheng Wang](https://dblp.org/pid/85/1868-1.html), [Xinliang Zhu](https://dblp.org/pid/160/9968.html), [Chaochao Yan](https://dblp.org/pid/223/4751.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

Label-Driven Reconstruction for Domain Adaptation in Semantic Segmentation. [CoRRabs/2003.04614](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-04614) (2020)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Chaochao Yan](https://dblp.org/pid/223/4751.html), [Qianggang Ding](https://dblp.org/pid/247/1295.html), [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Shuangjia Zheng](https://dblp.org/pid/235/3743.html), Jinyu Yang, [Yang Yu](https://dblp.org/pid/46/2181-10.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

RetroXpert: Decompose Retrosynthesis Prediction like a Chemist. [CoRRabs/2011.02893](https://dblp.org/db/journals/corr/corr2011.html#journals/corr/abs-2011-02893) (2020)
- ![](https://dblp.org/img/n.png)

\[i6\]
Jinyu Yang, [Peilin Zhao](https://dblp.org/pid/84/8411.html), [Yu Rong](https://dblp.org/pid/24/10036-1.html), [Chaochao Yan](https://dblp.org/pid/223/4751.html), [Chunyuan Li](https://dblp.org/pid/64/9590.html), [Hehuan Ma](https://dblp.org/pid/263/2003.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

Hierarchical Graph Capsule Network. [CoRRabs/2012.08734](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-08734) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[i5\]
Jinyu Yang, [Bo Zhang](https://dblp.org/pid/36/2259.html):

Artificial Intelligence in Intelligent Tutoring Robots: A Systematic Review and Design Guidelines. [CoRRabs/1903.03414](https://dblp.org/db/journals/corr/corr1903.html#journals/corr/abs-1903-03414) (2019)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Gaoyang Li](https://dblp.org/pid/98/7762.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang, [Chunguo Wu](https://dblp.org/pid/45/2669.html), [Qin Ma](https://dblp.org/pid/78/5428-3.html):

Maximal Margin Distribution Support Vector Regression with coupled Constraints-based Convex Optimization. [CoRRabs/1905.01620](https://dblp.org/db/journals/corr/corr1905.html#journals/corr/abs-1905-01620) (2019)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Chaochao Yan](https://dblp.org/pid/223/4751.html), [Sheng Wang](https://dblp.org/pid/85/1868-1.html), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Tingyang Xu](https://dblp.org/pid/157/0940.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html):

Re-balancing Variational Autoencoder Loss for Molecule Sequence Generation. [CoRRabs/1910.00698](https://dblp.org/db/journals/corr/corr1910.html#journals/corr/abs-1910-00698) (2019)
- ![](https://dblp.org/img/n.png)

\[i2\]
[Chunlei Liu](https://dblp.org/pid/76/5853-1.html), [Wenrui Ding](https://dblp.org/pid/08/10143.html), Jinyu Yang, [Vittorio Murino](https://dblp.org/pid/62/6790.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Jungong Han](https://dblp.org/pid/98/6127.html), [Guodong Guo](https://dblp.org/pid/92/4520.html):

Aggregation Signature for Small Object Tracking. [CoRRabs/1910.10859](https://dblp.org/db/journals/corr/corr1910.html#journals/corr/abs-1910-10859) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j7\]
[Sheng-Yong Niu](https://dblp.org/pid/219/4957.html), Jinyu Yang, [Adam McDermaid](https://dblp.org/pid/209/7127.html), [Jing Zhao](https://dblp.org/pid/69/5882.html), [Yu Kang](https://dblp.org/pid/98/3089-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qin Ma](https://dblp.org/pid/78/5428-3.html):

Bioinformatics tools for quantitative and functional metagenome and metatranscriptome data analysis in microbes. [Briefings Bioinform.19(2)](https://dblp.org/db/journals/bib/bib19.html#journals/bib/NiuYMZKM18): 360 (2018)
- ![](https://dblp.org/img/n.png)

\[j6\]
[Bingqiang Liu](https://dblp.org/pid/14/3443.html), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Li](https://dblp.org/pid/37/4190-89.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Adam McDermaid](https://dblp.org/pid/209/7127.html), [Qin Ma](https://dblp.org/pid/78/5428-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

An algorithmic perspective of de novo cis-regulatory motif finding based on ChIP-seq data. [Briefings Bioinform.19(5)](https://dblp.org/db/journals/bib/bib19.html#journals/bib/LiuYLMM18): 1069-1081 (2018)
- ![](https://dblp.org/img/n.png)

\[j5\]
[Sheng-Yong Niu](https://dblp.org/pid/219/4957.html), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Adam McDermaid](https://dblp.org/pid/209/7127.html), [Jing Zhao](https://dblp.org/pid/69/5882.html), [Yu Kang](https://dblp.org/pid/98/3089-4.html), [Qin Ma](https://dblp.org/pid/78/5428-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Bioinformatics tools for quantitative and functional metagenome and metatranscriptome data analysis in microbes. [Briefings Bioinform.19(6)](https://dblp.org/db/journals/bib/bib19.html#journals/bib/NiuYMZK018): 1415-1429 (2018)
- ![](https://dblp.org/img/n.png)

\[c4\]
Jinyu Yang, [Ru Chen](https://dblp.org/pid/52/3898.html), [Guozhou Zhang](https://dblp.org/pid/230/2465.html), [Hong Peng](https://dblp.org/pid/27/1817-1.html), [Jun Wang](https://dblp.org/pid/w/JunWang13.html), [Agustín Riscos-Núñez](https://dblp.org/pid/89/6274.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Kernel-Based Membrane Clustering Algorithm. [Enjoying Natural Computing2018](https://dblp.org/db/conf/birthday/PerezJimenez2018.html#conf/birthday/YangCZ0WR18): 318-329
- ![](https://dblp.org/img/n.png)

\[c3\]
[Longyin Wen](https://dblp.org/pid/119/1468.html), [Pengfei Zhu](https://dblp.org/pid/40/6172-1.html), [Dawei Du](https://dblp.org/pid/51/6958.html), [Xiao Bian](https://dblp.org/pid/116/5018.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Qinghua Hu](https://dblp.org/pid/30/2395.html), [Chenfeng Liu](https://dblp.org/pid/174/4324.html), [Hao Cheng](https://dblp.org/pid/09/5158-10.html), [Xiaoyu Liu](https://dblp.org/pid/78/6195-5.html), [Wenya Ma](https://dblp.org/pid/180/7077.html), [Qinqin Nie](https://dblp.org/pid/234/1733.html), [Haotian Wu](https://dblp.org/pid/145/5323-6.html), [Lianjie Wang](https://dblp.org/pid/18/2688.html), [Asanka G. Perera](https://dblp.org/pid/231/9229.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Byeongho Heo](https://dblp.org/pid/142/2705.html), [Chunlei Liu](https://dblp.org/pid/76/5853-1.html), [Dongdong Li](https://dblp.org/pid/14/5457.html), [Emmanouil Michail](https://dblp.org/pid/72/7219.html), [Hanlin Chen](https://dblp.org/pid/97/1735.html), [Hao Liu](https://dblp.org/pid/09/3214-19.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haojie Li](https://dblp.org/pid/61/4041.html), [Ioannis Kompatsiaris](https://dblp.org/pid/k/YiannisKompatsiaris.html), [Jian Cheng](https://dblp.org/pid/14/6145-1.html), [Jiaqing Fan](https://dblp.org/pid/227/6586.html), [Jie Zhang](https://dblp.org/pid/84/6889-91.html), [Jin Young Choi](https://dblp.org/pid/30/1428-2.html), [Jing Li](https://dblp.org/pid/l/JingLi36.html), Jinyu Yang, [Jongwon Choi](https://dblp.org/pid/126/0675-2.html), [Juanping Zhao](https://dblp.org/pid/120/5177.html), [Jungong Han](https://dblp.org/pid/98/6127.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kaiwen Duan](https://dblp.org/pid/190/4878.html), [Ke Song](https://dblp.org/pid/194/3688-3.html), [Konstantinos Avgerinakis](https://dblp.org/pid/15/10110.html), [Kyuewang Lee](https://dblp.org/pid/189/5760.html), [Lu Ding](https://dblp.org/pid/135/0285.html), [Martin Lauer](https://dblp.org/pid/87/2031.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Panagiotis Giannakeris](https://dblp.org/pid/213/4135.html), [Peizhen Zhang](https://dblp.org/pid/115/9027.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Qianqian Xu](https://dblp.org/pid/07/7627-1.html), [Qingming Huang](https://dblp.org/pid/68/4388.html), [Qingshan Liu](https://dblp.org/pid/95/1247.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Robert Laganière](https://dblp.org/pid/32/1448.html), [Ruixin Zhang](https://dblp.org/pid/132/6250.html), [Sangdoo Yun](https://dblp.org/pid/124/3009.html), [Shengyin Zhu](https://dblp.org/pid/234/1707.html), [Sihang Wu](https://dblp.org/pid/234/0006.html), [Stefanos Vrochidis](https://dblp.org/pid/44/6029.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Tian](https://dblp.org/pid/56/3860-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Zhang](https://dblp.org/pid/10/4661-21.html), [Weidong Chen](https://dblp.org/pid/196/5142-13.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wenhao Wang](https://dblp.org/pid/57/9813.html), [Wenhua Zhang](https://dblp.org/pid/28/1877.html), [Wenrui Ding](https://dblp.org/pid/08/10143.html), [Xiaohao He](https://dblp.org/pid/219/4446.html), [Xiaotong Li](https://dblp.org/pid/35/4953.html), [Xin Zhang](https://dblp.org/pid/76/1584-8.html), [Xinbin Luo](https://dblp.org/pid/234/1736.html), [Xixi Hu](https://dblp.org/pid/234/1710-3.html), [Yang Meng](https://dblp.org/pid/41/7386.html), [Yangliu Kuai](https://dblp.org/pid/202/5604.html), [Yanyun Zhao](https://dblp.org/pid/12/7547.html), [Yaxuan Li](https://dblp.org/pid/92/6967.html), [Yifan Yang](https://dblp.org/pid/83/89.html), [Yifan Zhang](https://dblp.org/pid/57/4707-1.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yuankai Qi](https://dblp.org/pid/136/5491.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhipeng Deng](https://dblp.org/pid/30/10701.html), [Zhiqun He](https://dblp.org/pid/213/4141.html):

VisDrone-SOT2018: The Vision Meets Drone Single-Object Tracking Challenge Results. [ECCV Workshops (5)2018](https://dblp.org/db/conf/eccv/eccv2018w5.html#conf/eccv/WenZDBLHLCLMNWW18): 469-495
- ![](https://dblp.org/img/n.png)

\[c2\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Wenrui Ding](https://dblp.org/pid/08/10143.html), [Chunlei Liu](https://dblp.org/pid/76/5853-1.html), [Zechen Ha](https://dblp.org/pid/229/1288.html):

A Saliency-Based Object Tracking Method for UAV Application. [PRCV (4)2018](https://dblp.org/db/conf/prcv/prcv2018-4.html#conf/prcv/YangDLH18): 115-125
- ![](https://dblp.org/img/n.png)

\[i1\]
[Bo Zhang](https://dblp.org/pid/36/2259-15.html), [Bin Chen](https://dblp.org/pid/22/5523.html), Jinyu Yang, [Wenjing Yang](https://dblp.org/pid/48/3396.html), [Jiankang Zhang](https://dblp.org/pid/94/1861-1.html):

An Unified Intelligence-Communication Model for Multi-Agent System Part-I: Overview. [CoRRabs/1811.09920](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-09920) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j4\]
[Yu Zhang](https://dblp.org/pid/50/671.html), [Juan Xie](https://dblp.org/pid/29/10304.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Anne Fennell](https://dblp.org/pid/174/0401.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Zhang](https://dblp.org/pid/91/195-21.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qin Ma](https://dblp.org/pid/78/5428-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

QUBIC: a bioconductor package for qualitative biclustering analysis of gene co-expression data. [Bioinform.33(3)](https://dblp.org/db/journals/bioinformatics/bioinformatics33.html#journals/bioinformatics/ZhangXYFZM17): 450-452 (2017)
- ![](https://dblp.org/img/n.png)

\[j3\]
Jinyu Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Chen](https://dblp.org/pid/24/1518.html), [Adam McDermaid](https://dblp.org/pid/209/7127.html), [Qin Ma](https://dblp.org/pid/78/5428-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DMINDA 2.0: integrated and systematic views of regulatory DNA motif identification and analyses. [Bioinform.33(16)](https://dblp.org/db/journals/bioinformatics/bioinformatics33.html#journals/bioinformatics/YangCMM17): 2586-2588 (2017)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Hong Peng](https://dblp.org/pid/27/1817-1.html), Jinyu Yang, [Jun Wang](https://dblp.org/pid/w/JunWang13.html), [Tao Wang](https://dblp.org/pid/12/5838-29.html), [Zhang Sun](https://dblp.org/pid/151/5901.html), [Xiaoxiao Song](https://dblp.org/pid/93/1045.html), [Xiaohui Luo](https://dblp.org/pid/121/5533.html), [Xiangnian Huang](https://dblp.org/pid/192/7624.html):

Spiking neural P systems with multiple channels. [Neural Networks95](https://dblp.org/db/journals/nn/nn95.html#journals/nn/PengYWWSSLH17): 66-71 (2017)
- 2014
- ![](https://dblp.org/img/n.png)

\[j1\]
[Hengzhen Huang](https://dblp.org/pid/138/6467.html), Jinyu Yang, [Min-Qian Liu](https://dblp.org/pid/28/1560.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Functionally induced priors for componentwise Gibbs sampler in the analysis of supersaturated designs. [Comput. Stat. Data Anal.72](https://dblp.org/db/journals/csda/csda72.html#journals/csda/HuangYL14): 1-12 (2014)
- ![](https://dblp.org/img/n.png)

\[c1\]
[Qiuying Li](https://dblp.org/pid/61/5550.html), [Gaoyang Li](https://dblp.org/pid/98/7762.html), [Xiaosong Han](https://dblp.org/pid/34/8578.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianping Zhang](https://dblp.org/pid/03/2548.html), [Yanchun Liang](https://dblp.org/pid/77/175-1.html), [Binghong Wang](https://dblp.org/pid/83/7132.html), [Hong Li](https://dblp.org/pid/93/6234.html), Jinyu Yang, [Chunguo Wu](https://dblp.org/pid/45/2669.html):

Global prediction-based adaptive mutation particle swarm optimization. [ICNC2014](https://dblp.org/db/conf/icnc/icnc2014.html#conf/icnc/LiLHZLWLYW14): 268-273
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/138/6456.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[2](https://dblp.org/pid/138/6456.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Weizhi An](https://dblp.org/pid/224/2525.html)

[\[c23\]](https://dblp.org/pid/138/6456.html#c23) [\[c13\]](https://dblp.org/pid/138/6456.html#c13) [\[c10\]](https://dblp.org/pid/138/6456.html#c10) [\[i13\]](https://dblp.org/pid/138/6456.html#i13) [\[c7\]](https://dblp.org/pid/138/6456.html#c7) [\[i9\]](https://dblp.org/pid/138/6456.html#i9) [\[i8\]](https://dblp.org/pid/138/6456.html#i8)

[3](https://dblp.org/pid/138/6456.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tarik Arici](https://dblp.org/pid/14/5731.html)

[\[c28\]](https://dblp.org/pid/138/6456.html#c28)

[4](https://dblp.org/pid/138/6456.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Minasadat Attari](https://dblp.org/pid/370/3618.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[5](https://dblp.org/pid/138/6456.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Konstantinos Avgerinakis](https://dblp.org/pid/15/10110.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[6](https://dblp.org/pid/138/6456.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dongdong Bai](https://dblp.org/pid/196/7870.html)

[\[j24\]](https://dblp.org/pid/138/6456.html#j24)

[7](https://dblp.org/pid/138/6456.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Haoran Bai](https://dblp.org/pid/235/9510.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[8](https://dblp.org/pid/138/6456.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Huihui Bai 0003](https://dblp.org/pid/75/5070-3.html)

[\[c29\]](https://dblp.org/pid/138/6456.html#c29)

[9](https://dblp.org/pid/138/6456.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Song Bai 0001](https://dblp.org/pid/151/6422-1.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[10](https://dblp.org/pid/138/6456.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[11](https://dblp.org/pid/138/6456.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Luca Bertinetto](https://dblp.org/pid/154/1351.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[12](https://dblp.org/pid/138/6456.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jesús Bescós](https://dblp.org/pid/97/2333.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[13](https://dblp.org/pid/138/6456.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[14](https://dblp.org/pid/138/6456.html?view=joint&param=14 "show joint publications")

[Qingqing Bi](https://dblp.org/pid/41/10676.html)

[\[j16\]](https://dblp.org/pid/138/6456.html#j16)

[15](https://dblp.org/pid/138/6456.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiao Bian](https://dblp.org/pid/116/5018.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[16](https://dblp.org/pid/138/6456.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yatao Bian](https://dblp.org/pid/222/2694.html)

[\[c23\]](https://dblp.org/pid/138/6456.html#c23)

[17](https://dblp.org/pid/138/6456.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Anuj Bindal](https://dblp.org/pid/383/9891.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[18](https://dblp.org/pid/138/6456.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[19](https://dblp.org/pid/138/6456.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Rainer Burgkart](https://dblp.org/pid/40/5566.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[20](https://dblp.org/pid/138/6456.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[21](https://dblp.org/pid/138/6456.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yi Cai 0001](https://dblp.org/pid/58/3467-1.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31) [\[i29\]](https://dblp.org/pid/138/6456.html#i29)

[22](https://dblp.org/pid/138/6456.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bin Cao](https://dblp.org/pid/17/1169.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[23](https://dblp.org/pid/138/6456.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[24](https://dblp.org/pid/138/6456.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[25](https://dblp.org/pid/138/6456.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[26](https://dblp.org/pid/138/6456.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tianhao Chai](https://dblp.org/pid/421/2898.html)

[\[c39\]](https://dblp.org/pid/138/6456.html#c39)

[27](https://dblp.org/pid/138/6456.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Antoni B. Chan](https://dblp.org/pid/55/5814.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[28](https://dblp.org/pid/138/6456.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sampath Chanda](https://dblp.org/pid/244/2140.html)

[\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18)

[29](https://dblp.org/pid/138/6456.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[30](https://dblp.org/pid/138/6456.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c20\]](https://dblp.org/pid/138/6456.html#c20) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[31](https://dblp.org/pid/138/6456.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bin Chen](https://dblp.org/pid/22/5523.html)

[\[i1\]](https://dblp.org/pid/138/6456.html#i1)

[32](https://dblp.org/pid/138/6456.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[33](https://dblp.org/pid/138/6456.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hanlin Chen](https://dblp.org/pid/97/1735.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[34](https://dblp.org/pid/138/6456.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jia Chen](https://dblp.org/pid/99/6879.html)

[\[j22\]](https://dblp.org/pid/138/6456.html#j22)

[35](https://dblp.org/pid/138/6456.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiali Chen](https://dblp.org/pid/14/2352.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31) [\[i29\]](https://dblp.org/pid/138/6456.html#i29)

[36](https://dblp.org/pid/138/6456.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jianpeng Chen](https://dblp.org/pid/234/5858.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31)

[37](https://dblp.org/pid/138/6456.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[38](https://dblp.org/pid/138/6456.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kelvin Chen](https://dblp.org/pid/187/0349.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[39](https://dblp.org/pid/138/6456.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liang Chen](https://dblp.org/pid/01/5394.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[40](https://dblp.org/pid/138/6456.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liqun Chen 0001](https://dblp.org/pid/22/150-1.html)

[\[c22\]](https://dblp.org/pid/138/6456.html#c22) [\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18) [\[i17\]](https://dblp.org/pid/138/6456.html#i17)

[41](https://dblp.org/pid/138/6456.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Peng Chen](https://dblp.org/pid/27/7017.html)

[\[i22\]](https://dblp.org/pid/138/6456.html#i22) [\[c25\]](https://dblp.org/pid/138/6456.html#c25)

[42](https://dblp.org/pid/138/6456.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ru Chen](https://dblp.org/pid/52/3898.html)

[\[c4\]](https://dblp.org/pid/138/6456.html#c4)

[43](https://dblp.org/pid/138/6456.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[44](https://dblp.org/pid/138/6456.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shuhao Chen](https://dblp.org/pid/43/2127.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[45](https://dblp.org/pid/138/6456.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Weidong Chen 0013](https://dblp.org/pid/196/5142-13.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[46](https://dblp.org/pid/138/6456.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[47](https://dblp.org/pid/138/6456.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xin Chen](https://dblp.org/pid/24/1518.html)

[\[j3\]](https://dblp.org/pid/138/6456.html#j3)

[48](https://dblp.org/pid/138/6456.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[49](https://dblp.org/pid/138/6456.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[50](https://dblp.org/pid/138/6456.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[51](https://dblp.org/pid/138/6456.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[52](https://dblp.org/pid/138/6456.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[53](https://dblp.org/pid/138/6456.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ziwei Chen](https://dblp.org/pid/219/9605.html)

[\[i30\]](https://dblp.org/pid/138/6456.html#i30)

[54](https://dblp.org/pid/138/6456.html?view=joint&param=54 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=2)

[Gordon Cheng](https://dblp.org/pid/03/2800.html)

[\[i28\]](https://dblp.org/pid/138/6456.html#i28)

[55](https://dblp.org/pid/138/6456.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hao Cheng 0010](https://dblp.org/pid/09/5158-10.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[56](https://dblp.org/pid/138/6456.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jian Cheng 0001](https://dblp.org/pid/14/6145-1.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[57](https://dblp.org/pid/138/6456.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Li Cheng 0001](https://dblp.org/pid/13/4938-1.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[58](https://dblp.org/pid/138/6456.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[59](https://dblp.org/pid/138/6456.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[60](https://dblp.org/pid/138/6456.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[61](https://dblp.org/pid/138/6456.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Trishul Chilimbi](https://dblp.org/pid/265/6085.html)

[\[c41\]](https://dblp.org/pid/138/6456.html#c41) [\[i36\]](https://dblp.org/pid/138/6456.html#i36) [\[c36\]](https://dblp.org/pid/138/6456.html#c36) [\[i24\]](https://dblp.org/pid/138/6456.html#i24) [\[c22\]](https://dblp.org/pid/138/6456.html#c22) [\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18) [\[i17\]](https://dblp.org/pid/138/6456.html#i17)

[62](https://dblp.org/pid/138/6456.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[63](https://dblp.org/pid/138/6456.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jin Young Choi 0002](https://dblp.org/pid/30/1428-2.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[64](https://dblp.org/pid/138/6456.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jongwon Choi 0002](https://dblp.org/pid/126/0675-2.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[65](https://dblp.org/pid/138/6456.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Seokeon Choi](https://dblp.org/pid/214/2200.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[66](https://dblp.org/pid/138/6456.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[67](https://dblp.org/pid/138/6456.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[68](https://dblp.org/pid/138/6456.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jaired Collins](https://dblp.org/pid/211/4242.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[69](https://dblp.org/pid/138/6456.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Runmin Cong](https://dblp.org/pid/180/7852.html)

[\[j17\]](https://dblp.org/pid/138/6456.html#j17)

[70](https://dblp.org/pid/138/6456.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[71](https://dblp.org/pid/138/6456.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liu Cui](https://dblp.org/pid/143/0951.html)

[\[j18\]](https://dblp.org/pid/138/6456.html#j18) [\[c33\]](https://dblp.org/pid/138/6456.html#c33)

[72](https://dblp.org/pid/138/6456.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shanyuan Cui](https://dblp.org/pid/409/8702.html)

[\[i34\]](https://dblp.org/pid/138/6456.html#i34)

[73](https://dblp.org/pid/138/6456.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[74](https://dblp.org/pid/138/6456.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[75](https://dblp.org/pid/138/6456.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[76](https://dblp.org/pid/138/6456.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[77](https://dblp.org/pid/138/6456.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[78](https://dblp.org/pid/138/6456.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhipeng Deng](https://dblp.org/pid/30/10701.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[79](https://dblp.org/pid/138/6456.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ganesh Sai Manas Devarapu](https://dblp.org/pid/406/4906.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[80](https://dblp.org/pid/138/6456.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[81](https://dblp.org/pid/138/6456.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Arnab Dhua](https://dblp.org/pid/96/2760.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[82](https://dblp.org/pid/138/6456.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[83](https://dblp.org/pid/138/6456.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Han Ding 0004](https://dblp.org/pid/88/886-4.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[84](https://dblp.org/pid/138/6456.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Henghui Ding](https://dblp.org/pid/230/1216.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[85](https://dblp.org/pid/138/6456.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Lu Ding](https://dblp.org/pid/135/0285.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[86](https://dblp.org/pid/138/6456.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qianggang Ding](https://dblp.org/pid/247/1295.html)

[\[c5\]](https://dblp.org/pid/138/6456.html#c5) [\[i7\]](https://dblp.org/pid/138/6456.html#i7)

[87](https://dblp.org/pid/138/6456.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tongsheng Ding](https://dblp.org/pid/394/9084.html)

[\[i33\]](https://dblp.org/pid/138/6456.html#i33)

[88](https://dblp.org/pid/138/6456.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenrui Ding](https://dblp.org/pid/08/10143.html)

[\[j8\]](https://dblp.org/pid/138/6456.html#j8) [\[i2\]](https://dblp.org/pid/138/6456.html#i2) [\[c3\]](https://dblp.org/pid/138/6456.html#c3) [\[c2\]](https://dblp.org/pid/138/6456.html#c2)

[89](https://dblp.org/pid/138/6456.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[90](https://dblp.org/pid/138/6456.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[91](https://dblp.org/pid/138/6456.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[92](https://dblp.org/pid/138/6456.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dawei Du](https://dblp.org/pid/51/6958.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[93](https://dblp.org/pid/138/6456.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yinglong Du](https://dblp.org/pid/199/1274.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[94](https://dblp.org/pid/138/6456.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiali Duan](https://dblp.org/pid/187/1570.html)

[\[c22\]](https://dblp.org/pid/138/6456.html#c22) [\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18) [\[i17\]](https://dblp.org/pid/138/6456.html#i17)

[95](https://dblp.org/pid/138/6456.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kaiwen Duan](https://dblp.org/pid/190/4878.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[96](https://dblp.org/pid/138/6456.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[97](https://dblp.org/pid/138/6456.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[98](https://dblp.org/pid/138/6456.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Edonis Elshani](https://dblp.org/pid/385/2924.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[99](https://dblp.org/pid/138/6456.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Deng-Ping Fan](https://dblp.org/pid/205/3148.html)

[\[i22\]](https://dblp.org/pid/138/6456.html#i22)

[100](https://dblp.org/pid/138/6456.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[101](https://dblp.org/pid/138/6456.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiaqing Fan](https://dblp.org/pid/227/6586.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[102](https://dblp.org/pid/138/6456.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wan-Cyuan Fan](https://dblp.org/pid/300/5836.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[103](https://dblp.org/pid/138/6456.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hao Fang 0010](https://dblp.org/pid/06/2484-10.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[104](https://dblp.org/pid/138/6456.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[105](https://dblp.org/pid/138/6456.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[106](https://dblp.org/pid/138/6456.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[107](https://dblp.org/pid/138/6456.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Anne Fennell](https://dblp.org/pid/174/0401.html)

[\[j4\]](https://dblp.org/pid/138/6456.html#j4)

[108](https://dblp.org/pid/138/6456.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hakan Ferhatosmanoglu](https://dblp.org/pid/f/HFerhatosmanoglu.html)

[\[c28\]](https://dblp.org/pid/138/6456.html#c28)

[109](https://dblp.org/pid/138/6456.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[110](https://dblp.org/pid/138/6456.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Gian Luca Foresti](https://dblp.org/pid/93/5522.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[111](https://dblp.org/pid/138/6456.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jianlong Fu](https://dblp.org/pid/83/8692.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[112](https://dblp.org/pid/138/6456.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[113](https://dblp.org/pid/138/6456.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiayi Gao](https://dblp.org/pid/315/3227.html)

[\[c39\]](https://dblp.org/pid/138/6456.html#c39)

[114](https://dblp.org/pid/138/6456.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mingqi Gao 0003](https://dblp.org/pid/191/2698-3.html)

[\[i33\]](https://dblp.org/pid/138/6456.html#i33) [\[i30\]](https://dblp.org/pid/138/6456.html#i30) [\[j17\]](https://dblp.org/pid/138/6456.html#j17) [\[j14\]](https://dblp.org/pid/138/6456.html#j14) [\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[c32\]](https://dblp.org/pid/138/6456.html#c32) [\[i27\]](https://dblp.org/pid/138/6456.html#i27) [\[i26\]](https://dblp.org/pid/138/6456.html#i26) [\[i25\]](https://dblp.org/pid/138/6456.html#i25) [\[j11\]](https://dblp.org/pid/138/6456.html#j11) [\[i19\]](https://dblp.org/pid/138/6456.html#i19)

[115](https://dblp.org/pid/138/6456.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c26\]](https://dblp.org/pid/138/6456.html#c26) [\[i19\]](https://dblp.org/pid/138/6456.html#i19) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c18\]](https://dblp.org/pid/138/6456.html#c18) [\[i14\]](https://dblp.org/pid/138/6456.html#i14)

[116](https://dblp.org/pid/138/6456.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Álvaro García-Martín](https://dblp.org/pid/39/1542.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[117](https://dblp.org/pid/138/6456.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[118](https://dblp.org/pid/138/6456.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[119](https://dblp.org/pid/138/6456.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[120](https://dblp.org/pid/138/6456.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Panagiotis Giannakeris](https://dblp.org/pid/213/4135.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[121](https://dblp.org/pid/138/6456.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Claudio Glowalla](https://dblp.org/pid/303/2970.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[122](https://dblp.org/pid/138/6456.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[123](https://dblp.org/pid/138/6456.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[124](https://dblp.org/pid/138/6456.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Rama Krishna Sai S. Gorthi](https://dblp.org/pid/45/7595.html)

aka: Rama Krishna Sai Subrahmanyam Gorthi

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[125](https://dblp.org/pid/138/6456.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Raghav Goyal](https://dblp.org/pid/191/6034.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[126](https://dblp.org/pid/138/6456.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[127](https://dblp.org/pid/138/6456.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Douglas Gray 0001](https://dblp.org/pid/78/2781.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[128](https://dblp.org/pid/138/6456.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[129](https://dblp.org/pid/138/6456.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[130](https://dblp.org/pid/138/6456.html?view=joint&param=130 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=2)

[Julio Rogelio Guadarrama-Olvera](https://dblp.org/pid/141/7418.html)

[\[i28\]](https://dblp.org/pid/138/6456.html#i28)

[131](https://dblp.org/pid/138/6456.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[132](https://dblp.org/pid/138/6456.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Guodong Guo](https://dblp.org/pid/92/4520.html)

[\[j8\]](https://dblp.org/pid/138/6456.html#j8) [\[i2\]](https://dblp.org/pid/138/6456.html#i2)

[133](https://dblp.org/pid/138/6456.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qianqian Guo](https://dblp.org/pid/04/9458.html)

[\[j21\]](https://dblp.org/pid/138/6456.html#j21) [\[j20\]](https://dblp.org/pid/138/6456.html#j20) [\[j18\]](https://dblp.org/pid/138/6456.html#j18) [\[j10\]](https://dblp.org/pid/138/6456.html#j10)

[134](https://dblp.org/pid/138/6456.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[135](https://dblp.org/pid/138/6456.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuzhi Guo](https://dblp.org/pid/249/0479.html)

[\[c23\]](https://dblp.org/pid/138/6456.html#c23) [\[c13\]](https://dblp.org/pid/138/6456.html#c13) [\[i13\]](https://dblp.org/pid/138/6456.html#i13) [\[c8\]](https://dblp.org/pid/138/6456.html#c8)

[136](https://dblp.org/pid/138/6456.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zeyuan Guo](https://dblp.org/pid/395/4778.html)

[\[c39\]](https://dblp.org/pid/138/6456.html#c39) [\[i34\]](https://dblp.org/pid/138/6456.html#i34)

[137](https://dblp.org/pid/138/6456.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[138](https://dblp.org/pid/138/6456.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[139](https://dblp.org/pid/138/6456.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Fredrik Gustafsson](https://dblp.org/pid/394/4497.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[140](https://dblp.org/pid/138/6456.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zechen Ha](https://dblp.org/pid/229/1288.html)

[\[c2\]](https://dblp.org/pid/138/6456.html#c2)

[141](https://dblp.org/pid/138/6456.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sami Haddadin](https://dblp.org/pid/01/3198.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[142](https://dblp.org/pid/138/6456.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[143](https://dblp.org/pid/138/6456.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Raffay Hamid](https://dblp.org/pid/38/51.html)

[\[c41\]](https://dblp.org/pid/138/6456.html#c41) [\[i36\]](https://dblp.org/pid/138/6456.html#i36)

[144](https://dblp.org/pid/138/6456.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Genquan Han](https://dblp.org/pid/269/2129.html)

[\[j12\]](https://dblp.org/pid/138/6456.html#j12)

[145](https://dblp.org/pid/138/6456.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jungong Han](https://dblp.org/pid/98/6127.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i26\]](https://dblp.org/pid/138/6456.html#i26) [\[i25\]](https://dblp.org/pid/138/6456.html#i25) [\[j11\]](https://dblp.org/pid/138/6456.html#j11) [\[j8\]](https://dblp.org/pid/138/6456.html#j8) [\[i2\]](https://dblp.org/pid/138/6456.html#i2) [\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[146](https://dblp.org/pid/138/6456.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[147](https://dblp.org/pid/138/6456.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaosong Han](https://dblp.org/pid/34/8578.html)

[\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[148](https://dblp.org/pid/138/6456.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yue Hao 0001](https://dblp.org/pid/17/1995-1.html)

[\[j12\]](https://dblp.org/pid/138/6456.html#j12)

[149](https://dblp.org/pid/138/6456.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yunlai Hao](https://dblp.org/pid/358/7797.html)

[\[c29\]](https://dblp.org/pid/138/6456.html#c29)

[150](https://dblp.org/pid/138/6456.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bijaya Kumar Hatuwal](https://dblp.org/pid/318/9407.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[151](https://dblp.org/pid/138/6456.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Alex Hauptmann 0001](https://dblp.org/pid/h/AlexanderGHauptmann.html)

aka: Alexander G. Hauptmann

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[152](https://dblp.org/pid/138/6456.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[153](https://dblp.org/pid/138/6456.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[154](https://dblp.org/pid/138/6456.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Linbo He](https://dblp.org/pid/26/741.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[155](https://dblp.org/pid/138/6456.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shuting He](https://dblp.org/pid/255/9456.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[156](https://dblp.org/pid/138/6456.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaohao He](https://dblp.org/pid/219/4446.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[157](https://dblp.org/pid/138/6456.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xingjian He](https://dblp.org/pid/204/0216.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[158](https://dblp.org/pid/138/6456.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhenyu He 0001](https://dblp.org/pid/57/6240-1.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[159](https://dblp.org/pid/138/6456.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhiqun He](https://dblp.org/pid/213/4141.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[160](https://dblp.org/pid/138/6456.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xusen Hei](https://dblp.org/pid/389/2648.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31) [\[i29\]](https://dblp.org/pid/138/6456.html#i29)

[161](https://dblp.org/pid/138/6456.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Byeongho Heo](https://dblp.org/pid/142/2705.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[162](https://dblp.org/pid/138/6456.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiacheng Hou](https://dblp.org/pid/226/4634.html)

[\[j26\]](https://dblp.org/pid/138/6456.html#j26) [\[j15\]](https://dblp.org/pid/138/6456.html#j15)

[163](https://dblp.org/pid/138/6456.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qinghua Hu](https://dblp.org/pid/30/2395.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[164](https://dblp.org/pid/138/6456.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Weiming Hu 0004](https://dblp.org/pid/41/6824-4.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6) [\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[165](https://dblp.org/pid/138/6456.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiantao Hu](https://dblp.org/pid/160/8016.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[166](https://dblp.org/pid/138/6456.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xixi Hu 0003](https://dblp.org/pid/234/1710-3.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[167](https://dblp.org/pid/138/6456.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hai Huang](https://dblp.org/pid/51/944.html)

[\[c39\]](https://dblp.org/pid/138/6456.html#c39) [\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[168](https://dblp.org/pid/138/6456.html?view=joint&param=168 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=3)

[Hengzhen Huang](https://dblp.org/pid/138/6467.html)

[\[j1\]](https://dblp.org/pid/138/6456.html#j1)

[169](https://dblp.org/pid/138/6456.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jianzheng Huang](https://dblp.org/pid/402/1445.html)

[\[i37\]](https://dblp.org/pid/138/6456.html#i37)

[170](https://dblp.org/pid/138/6456.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Junzhou Huang](https://dblp.org/pid/22/1170.html)

[\[j13\]](https://dblp.org/pid/138/6456.html#j13) [\[c24\]](https://dblp.org/pid/138/6456.html#c24) [\[c23\]](https://dblp.org/pid/138/6456.html#c23) [\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18) [\[c15\]](https://dblp.org/pid/138/6456.html#c15) [\[c13\]](https://dblp.org/pid/138/6456.html#c13) [\[c10\]](https://dblp.org/pid/138/6456.html#c10) [\[i13\]](https://dblp.org/pid/138/6456.html#i13) [\[i12\]](https://dblp.org/pid/138/6456.html#i12) [\[c9\]](https://dblp.org/pid/138/6456.html#c9) [\[c8\]](https://dblp.org/pid/138/6456.html#c8) [\[c7\]](https://dblp.org/pid/138/6456.html#c7) [\[c5\]](https://dblp.org/pid/138/6456.html#c5) [\[i9\]](https://dblp.org/pid/138/6456.html#i9) [\[i8\]](https://dblp.org/pid/138/6456.html#i8) [\[i7\]](https://dblp.org/pid/138/6456.html#i7) [\[i6\]](https://dblp.org/pid/138/6456.html#i6) [\[i3\]](https://dblp.org/pid/138/6456.html#i3)

[171](https://dblp.org/pid/138/6456.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Michael Huang](https://dblp.org/pid/87/6759.html)

[\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[172](https://dblp.org/pid/138/6456.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qingming Huang](https://dblp.org/pid/68/4388.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[173](https://dblp.org/pid/138/6456.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sheng-Wei Huang](https://dblp.org/pid/67/6807.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30)

[174](https://dblp.org/pid/138/6456.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiangnian Huang](https://dblp.org/pid/192/7624.html)

[\[j2\]](https://dblp.org/pid/138/6456.html#j2)

[175](https://dblp.org/pid/138/6456.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xingsen Huang](https://dblp.org/pid/284/1333.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[176](https://dblp.org/pid/138/6456.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[177](https://dblp.org/pid/138/6456.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[178](https://dblp.org/pid/138/6456.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuqing Huang](https://dblp.org/pid/134/5853.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[179](https://dblp.org/pid/138/6456.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chuong Huynh](https://dblp.org/pid/289/7090.html)

[\[c41\]](https://dblp.org/pid/138/6456.html#c41) [\[i36\]](https://dblp.org/pid/138/6456.html#i36)

[180](https://dblp.org/pid/138/6456.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[181](https://dblp.org/pid/138/6456.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[182](https://dblp.org/pid/138/6456.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[j14\]](https://dblp.org/pid/138/6456.html#j14) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[183](https://dblp.org/pid/138/6456.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yugang Ji](https://dblp.org/pid/184/0823.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[184](https://dblp.org/pid/138/6456.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhong Ji](https://dblp.org/pid/36/6466.html)

[\[j26\]](https://dblp.org/pid/138/6456.html#j26) [\[j15\]](https://dblp.org/pid/138/6456.html#j15)

[185](https://dblp.org/pid/138/6456.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaole Jia](https://dblp.org/pid/358/3210.html)

[\[j12\]](https://dblp.org/pid/138/6456.html#j12)

[186](https://dblp.org/pid/138/6456.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yujie Jia](https://dblp.org/pid/241/5998.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31)

[187](https://dblp.org/pid/138/6456.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[188](https://dblp.org/pid/138/6456.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dongmei Jiang](https://dblp.org/pid/47/1926.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[189](https://dblp.org/pid/138/6456.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ying Jiang](https://dblp.org/pid/42/1709.html)

[\[j27\]](https://dblp.org/pid/138/6456.html#j27)

[190](https://dblp.org/pid/138/6456.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[191](https://dblp.org/pid/138/6456.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Licheng Jiao](https://dblp.org/pid/40/3714.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[192](https://dblp.org/pid/138/6456.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Teng Jin](https://dblp.org/pid/282/8285.html)

[\[c40\]](https://dblp.org/pid/138/6456.html#c40) [\[i21\]](https://dblp.org/pid/138/6456.html#i21)

[193](https://dblp.org/pid/138/6456.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yang Juan](https://dblp.org/pid/299/4372.html)

[\[c42\]](https://dblp.org/pid/138/6456.html#c42)

[194](https://dblp.org/pid/138/6456.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[195](https://dblp.org/pid/138/6456.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

aka: Joni-Kristian Kamarainen

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[i16\]](https://dblp.org/pid/138/6456.html#i16) [\[c14\]](https://dblp.org/pid/138/6456.html#c14) [\[c12\]](https://dblp.org/pid/138/6456.html#c12) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[i11\]](https://dblp.org/pid/138/6456.html#i11) [\[i10\]](https://dblp.org/pid/138/6456.html#i10) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[196](https://dblp.org/pid/138/6456.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ben Kang](https://dblp.org/pid/340/1671.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[197](https://dblp.org/pid/138/6456.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yu Kang 0004](https://dblp.org/pid/98/3089-4.html)

[\[j7\]](https://dblp.org/pid/138/6456.html#j7) [\[j5\]](https://dblp.org/pid/138/6456.html#j5)

[198](https://dblp.org/pid/138/6456.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[199](https://dblp.org/pid/138/6456.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c12\]](https://dblp.org/pid/138/6456.html#c12) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[i11\]](https://dblp.org/pid/138/6456.html#i11)

[200](https://dblp.org/pid/138/6456.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shohreh Kasaei](https://dblp.org/pid/78/5062.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[201](https://dblp.org/pid/138/6456.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[202](https://dblp.org/pid/138/6456.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Javad Khaghani](https://dblp.org/pid/233/0334.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[203](https://dblp.org/pid/138/6456.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[204](https://dblp.org/pid/138/6456.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[205](https://dblp.org/pid/138/6456.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[206](https://dblp.org/pid/138/6456.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Robin Jeanne Kirschner](https://dblp.org/pid/292/8686.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[207](https://dblp.org/pid/138/6456.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[208](https://dblp.org/pid/138/6456.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ioannis Kompatsiaris](https://dblp.org/pid/k/YiannisKompatsiaris.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[209](https://dblp.org/pid/138/6456.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[210](https://dblp.org/pid/138/6456.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yangliu Kuai](https://dblp.org/pid/202/5604.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[211](https://dblp.org/pid/138/6456.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[212](https://dblp.org/pid/138/6456.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kushal Kumar](https://dblp.org/pid/318/2740.html)

[\[c28\]](https://dblp.org/pid/138/6456.html#c28)

[213](https://dblp.org/pid/138/6456.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Robert Laganière](https://dblp.org/pid/32/1448.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[214](https://dblp.org/pid/138/6456.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[215](https://dblp.org/pid/138/6456.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[216](https://dblp.org/pid/138/6456.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Martin Lauer](https://dblp.org/pid/87/2031.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[217](https://dblp.org/pid/138/6456.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[218](https://dblp.org/pid/138/6456.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[219](https://dblp.org/pid/138/6456.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[220](https://dblp.org/pid/138/6456.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[221](https://dblp.org/pid/138/6456.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jun-Hyun Lee](https://dblp.org/pid/155/8661.html)

aka: Junhyun Lee

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[222](https://dblp.org/pid/138/6456.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kyuewang Lee](https://dblp.org/pid/189/5760.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[223](https://dblp.org/pid/138/6456.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[224](https://dblp.org/pid/138/6456.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yunsung Lee](https://dblp.org/pid/227/9311.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[225](https://dblp.org/pid/138/6456.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tobias Leibbrand](https://dblp.org/pid/385/3344.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[226](https://dblp.org/pid/138/6456.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[227](https://dblp.org/pid/138/6456.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[j17\]](https://dblp.org/pid/138/6456.html#j17) [\[j14\]](https://dblp.org/pid/138/6456.html#j14) [\[i22\]](https://dblp.org/pid/138/6456.html#i22) [\[i21\]](https://dblp.org/pid/138/6456.html#i21) [\[c26\]](https://dblp.org/pid/138/6456.html#c26) [\[c20\]](https://dblp.org/pid/138/6456.html#c20) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c18\]](https://dblp.org/pid/138/6456.html#c18) [\[c16\]](https://dblp.org/pid/138/6456.html#c16) [\[i16\]](https://dblp.org/pid/138/6456.html#i16) [\[i15\]](https://dblp.org/pid/138/6456.html#i15) [\[i14\]](https://dblp.org/pid/138/6456.html#i14) [\[c14\]](https://dblp.org/pid/138/6456.html#c14) [\[c12\]](https://dblp.org/pid/138/6456.html#c12) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[i11\]](https://dblp.org/pid/138/6456.html#i11) [\[i10\]](https://dblp.org/pid/138/6456.html#i10) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[228](https://dblp.org/pid/138/6456.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ao Li](https://dblp.org/pid/54/2788.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[229](https://dblp.org/pid/138/6456.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bing Li 0001](https://dblp.org/pid/13/2692-1.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[230](https://dblp.org/pid/138/6456.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chunyuan Li](https://dblp.org/pid/64/9590.html)

[\[c23\]](https://dblp.org/pid/138/6456.html#c23) [\[c15\]](https://dblp.org/pid/138/6456.html#c15) [\[c13\]](https://dblp.org/pid/138/6456.html#c13) [\[i13\]](https://dblp.org/pid/138/6456.html#i13) [\[i6\]](https://dblp.org/pid/138/6456.html#i6)

[231](https://dblp.org/pid/138/6456.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dongdong Li](https://dblp.org/pid/14/5457.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[232](https://dblp.org/pid/138/6456.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dongmei Li](https://dblp.org/pid/27/1131.html)

[\[j24\]](https://dblp.org/pid/138/6456.html#j24)

[233](https://dblp.org/pid/138/6456.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Gaoyang Li](https://dblp.org/pid/98/7762.html)

[\[i4\]](https://dblp.org/pid/138/6456.html#i4) [\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[234](https://dblp.org/pid/138/6456.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Haojie Li](https://dblp.org/pid/61/4041.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[235](https://dblp.org/pid/138/6456.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hong Li](https://dblp.org/pid/93/6234.html)

[\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[236](https://dblp.org/pid/138/6456.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Houqiang Li](https://dblp.org/pid/59/7017.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[237](https://dblp.org/pid/138/6456.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[238](https://dblp.org/pid/138/6456.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[239](https://dblp.org/pid/138/6456.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jing Li 0036](https://dblp.org/pid/l/JingLi36.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[240](https://dblp.org/pid/138/6456.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Lu Li](https://dblp.org/pid/72/2266.html)

[\[c33\]](https://dblp.org/pid/138/6456.html#c33)

[241](https://dblp.org/pid/138/6456.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[242](https://dblp.org/pid/138/6456.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ning Li 0044](https://dblp.org/pid/14/5410-44.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[243](https://dblp.org/pid/138/6456.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qing Li 0001](https://dblp.org/pid/181/2689-1.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31)

[244](https://dblp.org/pid/138/6456.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qiuying Li](https://dblp.org/pid/61/5550.html)

[\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[245](https://dblp.org/pid/138/6456.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tao Li](https://dblp.org/pid/75/4601.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[246](https://dblp.org/pid/138/6456.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[247](https://dblp.org/pid/138/6456.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[248](https://dblp.org/pid/138/6456.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[249](https://dblp.org/pid/138/6456.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[250](https://dblp.org/pid/138/6456.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaohai Li](https://dblp.org/pid/00/38.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[251](https://dblp.org/pid/138/6456.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaotong Li](https://dblp.org/pid/35/4953.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[252](https://dblp.org/pid/138/6456.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xin Li 0034](https://dblp.org/pid/09/1365-34.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[253](https://dblp.org/pid/138/6456.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yang Li 0089](https://dblp.org/pid/37/4190-89.html)

[\[j6\]](https://dblp.org/pid/138/6456.html#j6)

[254](https://dblp.org/pid/138/6456.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yaxuan Li](https://dblp.org/pid/92/6967.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[255](https://dblp.org/pid/138/6456.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[256](https://dblp.org/pid/138/6456.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c26\]](https://dblp.org/pid/138/6456.html#c26) [\[i19\]](https://dblp.org/pid/138/6456.html#i19) [\[c20\]](https://dblp.org/pid/138/6456.html#c20) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c18\]](https://dblp.org/pid/138/6456.html#c18) [\[c16\]](https://dblp.org/pid/138/6456.html#c16) [\[i16\]](https://dblp.org/pid/138/6456.html#i16) [\[i15\]](https://dblp.org/pid/138/6456.html#i15) [\[i14\]](https://dblp.org/pid/138/6456.html#i14)

[257](https://dblp.org/pid/138/6456.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Cheng Liang](https://dblp.org/pid/81/9078.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[258](https://dblp.org/pid/138/6456.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qiuwei Liang](https://dblp.org/pid/318/8564.html)

[\[j10\]](https://dblp.org/pid/138/6456.html#j10)

[259](https://dblp.org/pid/138/6456.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yanchun Liang 0001](https://dblp.org/pid/77/175-1.html)

[\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[260](https://dblp.org/pid/138/6456.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[261](https://dblp.org/pid/138/6456.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xuanxu Lin](https://dblp.org/pid/380/2324.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[262](https://dblp.org/pid/138/6456.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6) [\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[263](https://dblp.org/pid/138/6456.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bingqiang Liu](https://dblp.org/pid/14/3443.html)

[\[j6\]](https://dblp.org/pid/138/6456.html#j6)

[264](https://dblp.org/pid/138/6456.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[265](https://dblp.org/pid/138/6456.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[266](https://dblp.org/pid/138/6456.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chang Liu 0072](https://dblp.org/pid/52/5716-72.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[267](https://dblp.org/pid/138/6456.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chenfeng Liu](https://dblp.org/pid/174/4324.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[268](https://dblp.org/pid/138/6456.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chunlei Liu 0001](https://dblp.org/pid/76/5853-1.html)

[\[j8\]](https://dblp.org/pid/138/6456.html#j8) [\[i2\]](https://dblp.org/pid/138/6456.html#i2) [\[c3\]](https://dblp.org/pid/138/6456.html#c3) [\[c2\]](https://dblp.org/pid/138/6456.html#c2)

[269](https://dblp.org/pid/138/6456.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hao Liu 0019](https://dblp.org/pid/09/3214-19.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[270](https://dblp.org/pid/138/6456.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jing Liu 0001](https://dblp.org/pid/72/2590-1.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[271](https://dblp.org/pid/138/6456.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[272](https://dblp.org/pid/138/6456.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jingjing Liu](https://dblp.org/pid/30/3008.html)

[\[c24\]](https://dblp.org/pid/138/6456.html#c24) [\[i12\]](https://dblp.org/pid/138/6456.html#i12)

[273](https://dblp.org/pid/138/6456.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kaiwen Liu](https://dblp.org/pid/231/4262.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[274](https://dblp.org/pid/138/6456.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[275](https://dblp.org/pid/138/6456.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Luoqi Liu](https://dblp.org/pid/29/8842.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[276](https://dblp.org/pid/138/6456.html?view=joint&param=276 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=3)

[Min-Qian Liu](https://dblp.org/pid/28/1560.html)

[\[j19\]](https://dblp.org/pid/138/6456.html#j19) [\[j1\]](https://dblp.org/pid/138/6456.html#j1)

[277](https://dblp.org/pid/138/6456.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Peiyang Liu](https://dblp.org/pid/275/7551.html)

[\[c29\]](https://dblp.org/pid/138/6456.html#c29)

[278](https://dblp.org/pid/138/6456.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[279](https://dblp.org/pid/138/6456.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qingshan Liu 0001](https://dblp.org/pid/95/1247.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[280](https://dblp.org/pid/138/6456.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[281](https://dblp.org/pid/138/6456.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ting Liu 0018](https://dblp.org/pid/52/5150-18.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[282](https://dblp.org/pid/138/6456.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaoyu Liu 0005](https://dblp.org/pid/78/6195-5.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[283](https://dblp.org/pid/138/6456.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xinyu Liu](https://dblp.org/pid/98/738.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[284](https://dblp.org/pid/138/6456.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yan Liu](https://dblp.org/pid/150/4295.html)

[\[j12\]](https://dblp.org/pid/138/6456.html#j12)

[285](https://dblp.org/pid/138/6456.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yijian Liu](https://dblp.org/pid/40/6142.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[286](https://dblp.org/pid/138/6456.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ziling Liu](https://dblp.org/pid/328/8536.html)

[\[i37\]](https://dblp.org/pid/138/6456.html#i37) [\[i30\]](https://dblp.org/pid/138/6456.html#i30) [\[c32\]](https://dblp.org/pid/138/6456.html#c32) [\[i27\]](https://dblp.org/pid/138/6456.html#i27)

[287](https://dblp.org/pid/138/6456.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ziquan Liu](https://dblp.org/pid/207/9035.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[288](https://dblp.org/pid/138/6456.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[289](https://dblp.org/pid/138/6456.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Junru Lu](https://dblp.org/pid/194/4596.html)

[\[i33\]](https://dblp.org/pid/138/6456.html#i33)

[290](https://dblp.org/pid/138/6456.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ke Lu 0002](https://dblp.org/pid/33/1254-2.html)

[\[j11\]](https://dblp.org/pid/138/6456.html#j11)

[291](https://dblp.org/pid/138/6456.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[292](https://dblp.org/pid/138/6456.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiankai Lu](https://dblp.org/pid/153/2122.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[293](https://dblp.org/pid/138/6456.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zixuan Lu](https://dblp.org/pid/231/6422.html)

[\[j27\]](https://dblp.org/pid/138/6456.html#j27)

[294](https://dblp.org/pid/138/6456.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[295](https://dblp.org/pid/138/6456.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[296](https://dblp.org/pid/138/6456.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jingnan Luo](https://dblp.org/pid/379/6720.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i26\]](https://dblp.org/pid/138/6456.html#i26) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[297](https://dblp.org/pid/138/6456.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaohui Luo](https://dblp.org/pid/121/5533.html)

[\[j9\]](https://dblp.org/pid/138/6456.html#j9) [\[j2\]](https://dblp.org/pid/138/6456.html#j2)

[298](https://dblp.org/pid/138/6456.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xinbin Luo](https://dblp.org/pid/234/1736.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[299](https://dblp.org/pid/138/6456.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yifei Luo](https://dblp.org/pid/58/3045.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[300](https://dblp.org/pid/138/6456.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhen Luo](https://dblp.org/pid/93/1458.html)

[\[i33\]](https://dblp.org/pid/138/6456.html#i33)

[301](https://dblp.org/pid/138/6456.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[302](https://dblp.org/pid/138/6456.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[303](https://dblp.org/pid/138/6456.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hehuan Ma](https://dblp.org/pid/263/2003.html)

[\[j13\]](https://dblp.org/pid/138/6456.html#j13) [\[c23\]](https://dblp.org/pid/138/6456.html#c23) [\[c15\]](https://dblp.org/pid/138/6456.html#c15) [\[c13\]](https://dblp.org/pid/138/6456.html#c13) [\[i13\]](https://dblp.org/pid/138/6456.html#i13) [\[c8\]](https://dblp.org/pid/138/6456.html#c8) [\[i6\]](https://dblp.org/pid/138/6456.html#i6)

[304](https://dblp.org/pid/138/6456.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[305](https://dblp.org/pid/138/6456.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qin Ma 0003](https://dblp.org/pid/78/5428-3.html)

[\[i4\]](https://dblp.org/pid/138/6456.html#i4) [\[j7\]](https://dblp.org/pid/138/6456.html#j7) [\[j6\]](https://dblp.org/pid/138/6456.html#j6) [\[j5\]](https://dblp.org/pid/138/6456.html#j5) [\[j4\]](https://dblp.org/pid/138/6456.html#j4) [\[j3\]](https://dblp.org/pid/138/6456.html#j3)

[306](https://dblp.org/pid/138/6456.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenya Ma](https://dblp.org/pid/180/7077.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[307](https://dblp.org/pid/138/6456.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[308](https://dblp.org/pid/138/6456.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[309](https://dblp.org/pid/138/6456.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhijun Mai](https://dblp.org/pid/247/9401.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[310](https://dblp.org/pid/138/6456.html?view=joint&param=310 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[311](https://dblp.org/pid/138/6456.html?view=joint&param=311 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[312](https://dblp.org/pid/138/6456.html?view=joint&param=312 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[313](https://dblp.org/pid/138/6456.html?view=joint&param=313 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[314](https://dblp.org/pid/138/6456.html?view=joint&param=314 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Adam McDermaid](https://dblp.org/pid/209/7127.html)

[\[j7\]](https://dblp.org/pid/138/6456.html#j7) [\[j6\]](https://dblp.org/pid/138/6456.html#j6) [\[j5\]](https://dblp.org/pid/138/6456.html#j5) [\[j3\]](https://dblp.org/pid/138/6456.html#j3)

[315](https://dblp.org/pid/138/6456.html?view=joint&param=315 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shunqi Mei](https://dblp.org/pid/72/4243.html)

[\[j22\]](https://dblp.org/pid/138/6456.html#j22)

[316](https://dblp.org/pid/138/6456.html?view=joint&param=316 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[317](https://dblp.org/pid/138/6456.html?view=joint&param=317 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yang Meng](https://dblp.org/pid/41/7386.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[318](https://dblp.org/pid/138/6456.html?view=joint&param=318 "show joint publications")

[Paolo Mengoni](https://dblp.org/pid/147/6967.html)

[\[c17\]](https://dblp.org/pid/138/6456.html#c17)

[319](https://dblp.org/pid/138/6456.html?view=joint&param=319 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Deshui Miao](https://dblp.org/pid/307/5501.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[320](https://dblp.org/pid/138/6456.html?view=joint&param=320 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Emmanouil Michail](https://dblp.org/pid/72/7219.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[321](https://dblp.org/pid/138/6456.html?view=joint&param=321 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Carina Micheler](https://dblp.org/pid/327/5319.html)

aka: Carina M. Micheler

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[322](https://dblp.org/pid/138/6456.html?view=joint&param=322 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[323](https://dblp.org/pid/138/6456.html?view=joint&param=323 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xianyu Mo](https://dblp.org/pid/402/0908.html)

[\[i37\]](https://dblp.org/pid/138/6456.html#i37)

[324](https://dblp.org/pid/138/6456.html?view=joint&param=324 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[325](https://dblp.org/pid/138/6456.html?view=joint&param=325 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Juan David Mogollon](https://dblp.org/pid/325/7624.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[326](https://dblp.org/pid/138/6456.html?view=joint&param=326 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Giovanni Montana](https://dblp.org/pid/89/449.html)

[\[j11\]](https://dblp.org/pid/138/6456.html#j11)

[327](https://dblp.org/pid/138/6456.html?view=joint&param=327 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dirk Müller](https://dblp.org/pid/58/1717.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[328](https://dblp.org/pid/138/6456.html?view=joint&param=328 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Vittorio Murino](https://dblp.org/pid/62/6790.html)

[\[j8\]](https://dblp.org/pid/138/6456.html#j8) [\[i2\]](https://dblp.org/pid/138/6456.html#i2)

[329](https://dblp.org/pid/138/6456.html?view=joint&param=329 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[330](https://dblp.org/pid/138/6456.html?view=joint&param=330 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tal Neiman](https://dblp.org/pid/155/3492.html)

[\[c36\]](https://dblp.org/pid/138/6456.html#c36) [\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i24\]](https://dblp.org/pid/138/6456.html#i24) [\[i20\]](https://dblp.org/pid/138/6456.html#i20) [\[c28\]](https://dblp.org/pid/138/6456.html#c28)

[331](https://dblp.org/pid/138/6456.html?view=joint&param=331 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[332](https://dblp.org/pid/138/6456.html?view=joint&param=332 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qinqin Nie](https://dblp.org/pid/234/1733.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[333](https://dblp.org/pid/138/6456.html?view=joint&param=333 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sheng-Yong Niu](https://dblp.org/pid/219/4957.html)

[\[j7\]](https://dblp.org/pid/138/6456.html#j7) [\[j5\]](https://dblp.org/pid/138/6456.html#j5)

[334](https://dblp.org/pid/138/6456.html?view=joint&param=334 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[335](https://dblp.org/pid/138/6456.html?view=joint&param=335 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kannappan Palaniappan](https://dblp.org/pid/21/700.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[336](https://dblp.org/pid/138/6456.html?view=joint&param=336 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Feiyu Pan](https://dblp.org/pid/142/1276.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[337](https://dblp.org/pid/138/6456.html?view=joint&param=337 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[338](https://dblp.org/pid/138/6456.html?view=joint&param=338 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ziqi Pang](https://dblp.org/pid/255/9210.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[339](https://dblp.org/pid/138/6456.html?view=joint&param=339 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[340](https://dblp.org/pid/138/6456.html?view=joint&param=340 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[341](https://dblp.org/pid/138/6456.html?view=joint&param=341 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[342](https://dblp.org/pid/138/6456.html?view=joint&param=342 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hong Peng 0001](https://dblp.org/pid/27/1817-1.html)

[\[j9\]](https://dblp.org/pid/138/6456.html#j9) [\[c4\]](https://dblp.org/pid/138/6456.html#c4) [\[j2\]](https://dblp.org/pid/138/6456.html#j2)

[343](https://dblp.org/pid/138/6456.html?view=joint&param=343 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[344](https://dblp.org/pid/138/6456.html?view=joint&param=344 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Asanka G. Perera](https://dblp.org/pid/231/9229.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[345](https://dblp.org/pid/138/6456.html?view=joint&param=345 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[346](https://dblp.org/pid/138/6456.html?view=joint&param=346 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jaswanth Reddy Pochimireddy](https://dblp.org/pid/406/5059.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[347](https://dblp.org/pid/138/6456.html?view=joint&param=347 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Viktor Prutyanov](https://dblp.org/pid/245/3321.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[348](https://dblp.org/pid/138/6456.html?view=joint&param=348 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuankai Qi](https://dblp.org/pid/136/5491.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[349](https://dblp.org/pid/138/6456.html?view=joint&param=349 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chen Qian 0006](https://dblp.org/pid/70/3604-6.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[350](https://dblp.org/pid/138/6456.html?view=joint&param=350 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[351](https://dblp.org/pid/138/6456.html?view=joint&param=351 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xi Qiu](https://dblp.org/pid/115/5698.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[352](https://dblp.org/pid/138/6456.html?view=joint&param=352 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Gani Rahmon](https://dblp.org/pid/291/7224.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[353](https://dblp.org/pid/138/6456.html?view=joint&param=353 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Nader Rajaei](https://dblp.org/pid/227/8455.html)

[\[c31\]](https://dblp.org/pid/138/6456.html#c31) [\[i23\]](https://dblp.org/pid/138/6456.html#i23)

[354](https://dblp.org/pid/138/6456.html?view=joint&param=354 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[355](https://dblp.org/pid/138/6456.html?view=joint&param=355 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[356](https://dblp.org/pid/138/6456.html?view=joint&param=356 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Nikhila Ravi](https://dblp.org/pid/248/7650.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[357](https://dblp.org/pid/138/6456.html?view=joint&param=357 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Agustin Riscos-Núñez](https://dblp.org/pid/89/6274.html)

aka: Agustín Riscos-Núñez

[\[c4\]](https://dblp.org/pid/138/6456.html#c4)

[358](https://dblp.org/pid/138/6456.html?view=joint&param=358 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mamshad Nayeem Rizve](https://dblp.org/pid/260/4900.html)

[\[c36\]](https://dblp.org/pid/138/6456.html#c36) [\[i24\]](https://dblp.org/pid/138/6456.html#i24)

[359](https://dblp.org/pid/138/6456.html?view=joint&param=359 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[360](https://dblp.org/pid/138/6456.html?view=joint&param=360 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Aleksandr Romanov 0001](https://dblp.org/pid/239/5991.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[361](https://dblp.org/pid/138/6456.html?view=joint&param=361 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yu Rong 0001](https://dblp.org/pid/24/10036-1.html)

[\[c15\]](https://dblp.org/pid/138/6456.html#c15) [\[c13\]](https://dblp.org/pid/138/6456.html#c13) [\[i13\]](https://dblp.org/pid/138/6456.html#i13) [\[i6\]](https://dblp.org/pid/138/6456.html#i6)

[362](https://dblp.org/pid/138/6456.html?view=joint&param=362 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[363](https://dblp.org/pid/138/6456.html?view=joint&param=363 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shioulin Sam](https://dblp.org/pid/358/8004.html)

[\[c28\]](https://dblp.org/pid/138/6456.html#c28)

[364](https://dblp.org/pid/138/6456.html?view=joint&param=364 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Victor Sanchez](https://dblp.org/pid/96/2574.html)

[\[j25\]](https://dblp.org/pid/138/6456.html#j25) [\[i35\]](https://dblp.org/pid/138/6456.html#i35) [\[i33\]](https://dblp.org/pid/138/6456.html#i33)

[365](https://dblp.org/pid/138/6456.html?view=joint&param=365 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[366](https://dblp.org/pid/138/6456.html?view=joint&param=366 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Thomas B. Schön](https://dblp.org/pid/85/4891.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[367](https://dblp.org/pid/138/6456.html?view=joint&param=367 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mubarak Shah](https://dblp.org/pid/s/MubarakShah.html)

[\[c41\]](https://dblp.org/pid/138/6456.html#c41) [\[i36\]](https://dblp.org/pid/138/6456.html#i36) [\[c36\]](https://dblp.org/pid/138/6456.html#c36) [\[i24\]](https://dblp.org/pid/138/6456.html#i24)

[368](https://dblp.org/pid/138/6456.html?view=joint&param=368 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[369](https://dblp.org/pid/138/6456.html?view=joint&param=369 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[j14\]](https://dblp.org/pid/138/6456.html#j14) [\[i16\]](https://dblp.org/pid/138/6456.html#i16) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[370](https://dblp.org/pid/138/6456.html?view=joint&param=370 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[371](https://dblp.org/pid/138/6456.html?view=joint&param=371 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[372](https://dblp.org/pid/138/6456.html?view=joint&param=372 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[373](https://dblp.org/pid/138/6456.html?view=joint&param=373 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chuan Shi 0001](https://dblp.org/pid/64/3041-1.html)

[\[c42\]](https://dblp.org/pid/138/6456.html#c42) [\[c39\]](https://dblp.org/pid/138/6456.html#c39) [\[i34\]](https://dblp.org/pid/138/6456.html#i34) [\[i32\]](https://dblp.org/pid/138/6456.html#i32) [\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[374](https://dblp.org/pid/138/6456.html?view=joint&param=374 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liangtao Shi](https://dblp.org/pid/366/5426.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[375](https://dblp.org/pid/138/6456.html?view=joint&param=375 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yanjiao Shi](https://dblp.org/pid/154/1947.html)

[\[j27\]](https://dblp.org/pid/138/6456.html#j27) [\[j21\]](https://dblp.org/pid/138/6456.html#j21) [\[j20\]](https://dblp.org/pid/138/6456.html#j20) [\[j18\]](https://dblp.org/pid/138/6456.html#j18) [\[c33\]](https://dblp.org/pid/138/6456.html#c33) [\[j10\]](https://dblp.org/pid/138/6456.html#j10)

[376](https://dblp.org/pid/138/6456.html?view=joint&param=376 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Abhinav Shrivastava](https://dblp.org/pid/65/10572.html)

[\[c41\]](https://dblp.org/pid/138/6456.html#c41) [\[i36\]](https://dblp.org/pid/138/6456.html#i36)

[377](https://dblp.org/pid/138/6456.html?view=joint&param=377 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mennatullah Siam](https://dblp.org/pid/163/9048.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[378](https://dblp.org/pid/138/6456.html?view=joint&param=378 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Leonid Sigal](https://dblp.org/pid/09/4991.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[379](https://dblp.org/pid/138/6456.html?view=joint&param=379 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[380](https://dblp.org/pid/138/6456.html?view=joint&param=380 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Arun Kumar Sivapuram](https://dblp.org/pid/344/4532.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[381](https://dblp.org/pid/138/6456.html?view=joint&param=381 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Roman A. Solovyev](https://dblp.org/pid/163/3390.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[382](https://dblp.org/pid/138/6456.html?view=joint&param=382 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Elham Soltanikazemi](https://dblp.org/pid/318/1851.html)

aka: Elham Soltani Kazemi

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[383](https://dblp.org/pid/138/6456.html?view=joint&param=383 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jingkuan Song](https://dblp.org/pid/70/10575.html)

[\[c18\]](https://dblp.org/pid/138/6456.html#c18) [\[c16\]](https://dblp.org/pid/138/6456.html#c16) [\[i15\]](https://dblp.org/pid/138/6456.html#i15) [\[i14\]](https://dblp.org/pid/138/6456.html#i14)

[384](https://dblp.org/pid/138/6456.html?view=joint&param=384 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ke Song 0003](https://dblp.org/pid/194/3688-3.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[385](https://dblp.org/pid/138/6456.html?view=joint&param=385 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[386](https://dblp.org/pid/138/6456.html?view=joint&param=386 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[387](https://dblp.org/pid/138/6456.html?view=joint&param=387 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaoxiao Song](https://dblp.org/pid/93/1045.html)

[\[j2\]](https://dblp.org/pid/138/6456.html#j2)

[388](https://dblp.org/pid/138/6456.html?view=joint&param=388 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[389](https://dblp.org/pid/138/6456.html?view=joint&param=389 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[390](https://dblp.org/pid/138/6456.html?view=joint&param=390 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhang Sun](https://dblp.org/pid/151/5901.html)

[\[j2\]](https://dblp.org/pid/138/6456.html#j2)

[391](https://dblp.org/pid/138/6456.html?view=joint&param=391 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sirnam Swetha](https://dblp.org/pid/171/5561.html)

[\[c36\]](https://dblp.org/pid/138/6456.html#c36) [\[i24\]](https://dblp.org/pid/138/6456.html#i24)

[392](https://dblp.org/pid/138/6456.html?view=joint&param=392 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[393](https://dblp.org/pid/138/6456.html?view=joint&param=393 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ashish Tawari](https://dblp.org/pid/59/8617.html)

[\[c41\]](https://dblp.org/pid/138/6456.html#c41) [\[i36\]](https://dblp.org/pid/138/6456.html#i36)

[394](https://dblp.org/pid/138/6456.html?view=joint&param=394 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wei Tian 0001](https://dblp.org/pid/56/3860-1.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[395](https://dblp.org/pid/138/6456.html?view=joint&param=395 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[396](https://dblp.org/pid/138/6456.html?view=joint&param=396 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Pavel Tokmakov](https://dblp.org/pid/153/2264.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[397](https://dblp.org/pid/138/6456.html?view=joint&param=397 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[398](https://dblp.org/pid/138/6456.html?view=joint&param=398 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Imad Eddine Toubal](https://dblp.org/pid/292/6360.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[399](https://dblp.org/pid/138/6456.html?view=joint&param=399 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Khanh-Tung Tran](https://dblp.org/pid/359/3793.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[400](https://dblp.org/pid/138/6456.html?view=joint&param=400 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Son Tran](https://dblp.org/pid/19/2438.html)

[\[c41\]](https://dblp.org/pid/138/6456.html#c41) [\[i36\]](https://dblp.org/pid/138/6456.html#i36) [\[c36\]](https://dblp.org/pid/138/6456.html#c36) [\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i24\]](https://dblp.org/pid/138/6456.html#i24) [\[i20\]](https://dblp.org/pid/138/6456.html#i20) [\[c22\]](https://dblp.org/pid/138/6456.html#c22) [\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18) [\[i17\]](https://dblp.org/pid/138/6456.html#i17)

[401](https://dblp.org/pid/138/6456.html?view=joint&param=401 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[402](https://dblp.org/pid/138/6456.html?view=joint&param=402 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ismail B. Tutar](https://dblp.org/pid/17/5973.html)

[\[c28\]](https://dblp.org/pid/138/6456.html#c28)

[403](https://dblp.org/pid/138/6456.html?view=joint&param=403 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[404](https://dblp.org/pid/138/6456.html?view=joint&param=404 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[405](https://dblp.org/pid/138/6456.html?view=joint&param=405 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[406](https://dblp.org/pid/138/6456.html?view=joint&param=406 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=2)

[Camille Vindolet](https://dblp.org/pid/341/9857.html)

[\[i28\]](https://dblp.org/pid/138/6456.html#i28)

[407](https://dblp.org/pid/138/6456.html?view=joint&param=407 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[408](https://dblp.org/pid/138/6456.html?view=joint&param=408 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Stefanos Vrochidis](https://dblp.org/pid/44/6029.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[409](https://dblp.org/pid/138/6456.html?view=joint&param=409 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xuan-Son Vu](https://dblp.org/pid/151/8673.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[410](https://dblp.org/pid/138/6456.html?view=joint&param=410 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chen Wan](https://dblp.org/pid/293/0656.html)

[\[c40\]](https://dblp.org/pid/138/6456.html#c40)

[411](https://dblp.org/pid/138/6456.html?view=joint&param=411 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jia Wan 0001](https://dblp.org/pid/13/6504-1.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[412](https://dblp.org/pid/138/6456.html?view=joint&param=412 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Binghong Wang](https://dblp.org/pid/83/7132.html)

[\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[413](https://dblp.org/pid/138/6456.html?view=joint&param=413 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chengjie Wang 0001](https://dblp.org/pid/142/0008-1.html)

[\[j17\]](https://dblp.org/pid/138/6456.html#j17) [\[j15\]](https://dblp.org/pid/138/6456.html#j15)

[414](https://dblp.org/pid/138/6456.html?view=joint&param=414 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=3)

[Chunyan Wang](https://dblp.org/pid/287/5495.html)

[\[j28\]](https://dblp.org/pid/138/6456.html#j28) [\[j19\]](https://dblp.org/pid/138/6456.html#j19)

[415](https://dblp.org/pid/138/6456.html?view=joint&param=415 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[416](https://dblp.org/pid/138/6456.html?view=joint&param=416 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Fangjing Wang](https://dblp.org/pid/249/7437.html)

[\[i19\]](https://dblp.org/pid/138/6456.html#i19)

[417](https://dblp.org/pid/138/6456.html?view=joint&param=417 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Fangyi Wang](https://dblp.org/pid/163/9017.html)

[\[c40\]](https://dblp.org/pid/138/6456.html#c40) [\[c37\]](https://dblp.org/pid/138/6456.html#c37) [\[i21\]](https://dblp.org/pid/138/6456.html#i21) [\[c25\]](https://dblp.org/pid/138/6456.html#c25)

[418](https://dblp.org/pid/138/6456.html?view=joint&param=418 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[419](https://dblp.org/pid/138/6456.html?view=joint&param=419 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[420](https://dblp.org/pid/138/6456.html?view=joint&param=420 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jun Wang 0013](https://dblp.org/pid/w/JunWang13.html)

[\[j9\]](https://dblp.org/pid/138/6456.html#j9) [\[c4\]](https://dblp.org/pid/138/6456.html#c4) [\[j2\]](https://dblp.org/pid/138/6456.html#j2)

[421](https://dblp.org/pid/138/6456.html?view=joint&param=421 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[422](https://dblp.org/pid/138/6456.html?view=joint&param=422 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[423](https://dblp.org/pid/138/6456.html?view=joint&param=423 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Lianjie Wang](https://dblp.org/pid/18/2688.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[424](https://dblp.org/pid/138/6456.html?view=joint&param=424 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[425](https://dblp.org/pid/138/6456.html?view=joint&param=425 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[426](https://dblp.org/pid/138/6456.html?view=joint&param=426 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Lin Wang 0106](https://dblp.org/pid/17/6729-106.html)

[\[c29\]](https://dblp.org/pid/138/6456.html#c29)

[427](https://dblp.org/pid/138/6456.html?view=joint&param=427 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[428](https://dblp.org/pid/138/6456.html?view=joint&param=428 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liqiong Wang](https://dblp.org/pid/311/0165.html)

[\[c37\]](https://dblp.org/pid/138/6456.html#c37) [\[i21\]](https://dblp.org/pid/138/6456.html#i21)

[429](https://dblp.org/pid/138/6456.html?view=joint&param=429 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ning Wang 0020](https://dblp.org/pid/46/2005-20.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[430](https://dblp.org/pid/138/6456.html?view=joint&param=430 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[431](https://dblp.org/pid/138/6456.html?view=joint&param=431 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qiang Wang 0051](https://dblp.org/pid/64/5630-51.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6) [\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[432](https://dblp.org/pid/138/6456.html?view=joint&param=432 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qingwei Wang](https://dblp.org/pid/88/2321.html)

[\[i22\]](https://dblp.org/pid/138/6456.html#i22) [\[c25\]](https://dblp.org/pid/138/6456.html#c25)

[433](https://dblp.org/pid/138/6456.html?view=joint&param=433 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ruijia Wang](https://dblp.org/pid/138/8168.html)

[\[c42\]](https://dblp.org/pid/138/6456.html#c42)

[434](https://dblp.org/pid/138/6456.html?view=joint&param=434 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sen Wang](https://dblp.org/pid/69/6403.html)

[\[c29\]](https://dblp.org/pid/138/6456.html#c29)

[435](https://dblp.org/pid/138/6456.html?view=joint&param=435 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sheng Wang 0001](https://dblp.org/pid/85/1868-1.html)

[\[j13\]](https://dblp.org/pid/138/6456.html#j13) [\[c9\]](https://dblp.org/pid/138/6456.html#c9) [\[c7\]](https://dblp.org/pid/138/6456.html#c7) [\[i8\]](https://dblp.org/pid/138/6456.html#i8) [\[i3\]](https://dblp.org/pid/138/6456.html#i3)

[436](https://dblp.org/pid/138/6456.html?view=joint&param=436 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tao Wang 0029](https://dblp.org/pid/12/5838-29.html)

[\[j2\]](https://dblp.org/pid/138/6456.html#j2)

[437](https://dblp.org/pid/138/6456.html?view=joint&param=437 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenhao Wang](https://dblp.org/pid/57/9813.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[438](https://dblp.org/pid/138/6456.html?view=joint&param=438 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xinying Wang 0005](https://dblp.org/pid/06/3244-5.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[439](https://dblp.org/pid/138/6456.html?view=joint&param=439 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yaowei Wang 0001](https://dblp.org/pid/68/2992-1.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[440](https://dblp.org/pid/138/6456.html?view=joint&param=440 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yibo Wang](https://dblp.org/pid/25/4764.html)

[\[j12\]](https://dblp.org/pid/138/6456.html#j12)

[441](https://dblp.org/pid/138/6456.html?view=joint&param=441 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ying-Ming Wang](https://dblp.org/pid/59/605.html)

aka: Yingming Wang

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[442](https://dblp.org/pid/138/6456.html?view=joint&param=442 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[443](https://dblp.org/pid/138/6456.html?view=joint&param=443 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yu-Xiong Wang](https://dblp.org/pid/35/10700.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[444](https://dblp.org/pid/138/6456.html?view=joint&param=444 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[445](https://dblp.org/pid/138/6456.html?view=joint&param=445 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zezhou Wang](https://dblp.org/pid/204/1179.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[446](https://dblp.org/pid/138/6456.html?view=joint&param=446 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhiquan Wang](https://dblp.org/pid/18/5129.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[447](https://dblp.org/pid/138/6456.html?view=joint&param=447 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yunchao Wei](https://dblp.org/pid/118/5394.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[448](https://dblp.org/pid/138/6456.html?view=joint&param=448 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Longyin Wen](https://dblp.org/pid/119/1468.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[449](https://dblp.org/pid/138/6456.html?view=joint&param=449 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chengjing Wu](https://dblp.org/pid/379/5986.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[450](https://dblp.org/pid/138/6456.html?view=joint&param=450 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[451](https://dblp.org/pid/138/6456.html?view=joint&param=451 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chunguo Wu](https://dblp.org/pid/45/2669.html)

[\[i4\]](https://dblp.org/pid/138/6456.html#i4) [\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[452](https://dblp.org/pid/138/6456.html?view=joint&param=452 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[453](https://dblp.org/pid/138/6456.html?view=joint&param=453 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Haotian Wu 0006](https://dblp.org/pid/145/5323-6.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[454](https://dblp.org/pid/138/6456.html?view=joint&param=454 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiaxiang Wu 0001](https://dblp.org/pid/119/6799-1.html)

[\[c8\]](https://dblp.org/pid/138/6456.html#c8)

[455](https://dblp.org/pid/138/6456.html?view=joint&param=455 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jing Wu](https://dblp.org/pid/88/3604.html)

[\[c39\]](https://dblp.org/pid/138/6456.html#c39)

[456](https://dblp.org/pid/138/6456.html?view=joint&param=456 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[457](https://dblp.org/pid/138/6456.html?view=joint&param=457 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qiangqiang Wu](https://dblp.org/pid/193/1415.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[458](https://dblp.org/pid/138/6456.html?view=joint&param=458 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sihang Wu](https://dblp.org/pid/234/0006.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[459](https://dblp.org/pid/138/6456.html?view=joint&param=459 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

aka: Xiao-Jun Wu 0001

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[460](https://dblp.org/pid/138/6456.html?view=joint&param=460 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhirong Wu](https://dblp.org/pid/147/5025.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[461](https://dblp.org/pid/138/6456.html?view=joint&param=461 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zihan Wu](https://dblp.org/pid/354/8152.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31)

[462](https://dblp.org/pid/138/6456.html?view=joint&param=462 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zihao Xia](https://dblp.org/pid/382/4580.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[463](https://dblp.org/pid/138/6456.html?view=joint&param=463 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[464](https://dblp.org/pid/138/6456.html?view=joint&param=464 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiayuan Xie](https://dblp.org/pid/249/8382.html)

[\[c38\]](https://dblp.org/pid/138/6456.html#c38) [\[i31\]](https://dblp.org/pid/138/6456.html#i31)

[465](https://dblp.org/pid/138/6456.html?view=joint&param=465 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jinxia Xie](https://dblp.org/pid/294/3376.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[466](https://dblp.org/pid/138/6456.html?view=joint&param=466 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Juan Xie](https://dblp.org/pid/29/10304.html)

[\[j4\]](https://dblp.org/pid/138/6456.html#j4)

[467](https://dblp.org/pid/138/6456.html?view=joint&param=467 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ouye Xie](https://dblp.org/pid/382/3920.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[468](https://dblp.org/pid/138/6456.html?view=joint&param=468 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bin Xu](https://dblp.org/pid/69/7024.html)

[\[j22\]](https://dblp.org/pid/138/6456.html#j22)

[469](https://dblp.org/pid/138/6456.html?view=joint&param=469 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chenlong Xu](https://dblp.org/pid/315/8714.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[470](https://dblp.org/pid/138/6456.html?view=joint&param=470 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jingtao Xu](https://dblp.org/pid/119/1746.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[471](https://dblp.org/pid/138/6456.html?view=joint&param=471 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ning Xu](https://dblp.org/pid/04/5856.html)

[\[c24\]](https://dblp.org/pid/138/6456.html#c24) [\[i12\]](https://dblp.org/pid/138/6456.html#i12)

[472](https://dblp.org/pid/138/6456.html?view=joint&param=472 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qianqian Xu 0001](https://dblp.org/pid/07/7627-1.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[473](https://dblp.org/pid/138/6456.html?view=joint&param=473 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[474](https://dblp.org/pid/138/6456.html?view=joint&param=474 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tingyang Xu](https://dblp.org/pid/157/0940.html)

[\[c9\]](https://dblp.org/pid/138/6456.html#c9) [\[i3\]](https://dblp.org/pid/138/6456.html#i3)

[475](https://dblp.org/pid/138/6456.html?view=joint&param=475 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[476](https://dblp.org/pid/138/6456.html?view=joint&param=476 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[477](https://dblp.org/pid/138/6456.html?view=joint&param=477 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yi Xu 0011](https://dblp.org/pid/14/5580-11.html)

[\[c28\]](https://dblp.org/pid/138/6456.html#c28) [\[c22\]](https://dblp.org/pid/138/6456.html#c22) [\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18) [\[i17\]](https://dblp.org/pid/138/6456.html#i17)

[478](https://dblp.org/pid/138/6456.html?view=joint&param=478 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[479](https://dblp.org/pid/138/6456.html?view=joint&param=479 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuanyou Xu](https://dblp.org/pid/248/7663.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[480](https://dblp.org/pid/138/6456.html?view=joint&param=480 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhensong Xu](https://dblp.org/pid/149/5188.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[481](https://dblp.org/pid/138/6456.html?view=joint&param=481 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chaocan Xue](https://dblp.org/pid/334/6591.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[482](https://dblp.org/pid/138/6456.html?view=joint&param=482 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[483](https://dblp.org/pid/138/6456.html?view=joint&param=483 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[484](https://dblp.org/pid/138/6456.html?view=joint&param=484 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[485](https://dblp.org/pid/138/6456.html?view=joint&param=485 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bo Yan](https://dblp.org/pid/63/6796.html)

[\[c42\]](https://dblp.org/pid/138/6456.html#c42)

[486](https://dblp.org/pid/138/6456.html?view=joint&param=486 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chaochao Yan](https://dblp.org/pid/223/4751.html)

[\[j13\]](https://dblp.org/pid/138/6456.html#j13) [\[c15\]](https://dblp.org/pid/138/6456.html#c15) [\[c10\]](https://dblp.org/pid/138/6456.html#c10) [\[c9\]](https://dblp.org/pid/138/6456.html#c9) [\[c7\]](https://dblp.org/pid/138/6456.html#c7) [\[c5\]](https://dblp.org/pid/138/6456.html#c5) [\[i9\]](https://dblp.org/pid/138/6456.html#i9) [\[i8\]](https://dblp.org/pid/138/6456.html#i8) [\[i7\]](https://dblp.org/pid/138/6456.html#i7) [\[i6\]](https://dblp.org/pid/138/6456.html#i6) [\[i3\]](https://dblp.org/pid/138/6456.html#i3)

[487](https://dblp.org/pid/138/6456.html?view=joint&param=487 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[i16\]](https://dblp.org/pid/138/6456.html#i16) [\[c14\]](https://dblp.org/pid/138/6456.html#c14) [\[c12\]](https://dblp.org/pid/138/6456.html#c12) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[i11\]](https://dblp.org/pid/138/6456.html#i11) [\[i10\]](https://dblp.org/pid/138/6456.html#i10) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[488](https://dblp.org/pid/138/6456.html?view=joint&param=488 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chao Yang](https://dblp.org/pid/00/5867.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[489](https://dblp.org/pid/138/6456.html?view=joint&param=489 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Cheng Yang 0002](https://dblp.org/pid/49/1457-2.html)

[\[c42\]](https://dblp.org/pid/138/6456.html#c42) [\[c39\]](https://dblp.org/pid/138/6456.html#c39) [\[i34\]](https://dblp.org/pid/138/6456.html#i34) [\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[490](https://dblp.org/pid/138/6456.html?view=joint&param=490 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[491](https://dblp.org/pid/138/6456.html?view=joint&param=491 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Juan Yang](https://dblp.org/pid/22/815.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[492](https://dblp.org/pid/138/6456.html?view=joint&param=492 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kang Yang](https://dblp.org/pid/86/8501.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[493](https://dblp.org/pid/138/6456.html?view=joint&param=493 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Liangwei Yang](https://dblp.org/pid/260/5064.html)

[\[c39\]](https://dblp.org/pid/138/6456.html#c39) [\[i34\]](https://dblp.org/pid/138/6456.html#i34)

[494](https://dblp.org/pid/138/6456.html?view=joint&param=494 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ming-Hsuan Yang 0001](https://dblp.org/pid/79/3711.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[495](https://dblp.org/pid/138/6456.html?view=joint&param=495 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shuyuan Yang 0001](https://dblp.org/pid/81/2383.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[496](https://dblp.org/pid/138/6456.html?view=joint&param=496 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[497](https://dblp.org/pid/138/6456.html?view=joint&param=497 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenjing Yang](https://dblp.org/pid/48/3396.html)

[\[i1\]](https://dblp.org/pid/138/6456.html#i1)

[498](https://dblp.org/pid/138/6456.html?view=joint&param=498 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[499](https://dblp.org/pid/138/6456.html?view=joint&param=499 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[500](https://dblp.org/pid/138/6456.html?view=joint&param=500 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[501](https://dblp.org/pid/138/6456.html?view=joint&param=501 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[502](https://dblp.org/pid/138/6456.html?view=joint&param=502 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yifan Yang](https://dblp.org/pid/83/89.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[503](https://dblp.org/pid/138/6456.html?view=joint&param=503 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yixuan Yang](https://dblp.org/pid/229/1326.html)

[\[j25\]](https://dblp.org/pid/138/6456.html#j25) [\[i35\]](https://dblp.org/pid/138/6456.html#i35) [\[i33\]](https://dblp.org/pid/138/6456.html#i33)

[504](https://dblp.org/pid/138/6456.html?view=joint&param=504 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuting Yang 0008](https://dblp.org/pid/25/3635-8.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[505](https://dblp.org/pid/138/6456.html?view=joint&param=505 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[506](https://dblp.org/pid/138/6456.html?view=joint&param=506 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Benjamin Z. Yao](https://dblp.org/pid/134/7162.html)

[\[c36\]](https://dblp.org/pid/138/6456.html#c36) [\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i24\]](https://dblp.org/pid/138/6456.html#i24) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[507](https://dblp.org/pid/138/6456.html?view=joint&param=507 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiangtao Yao](https://dblp.org/pid/294/5962.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[508](https://dblp.org/pid/138/6456.html?view=joint&param=508 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yuncon Yao](https://dblp.org/pid/284/2556.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[509](https://dblp.org/pid/138/6456.html?view=joint&param=509 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[510](https://dblp.org/pid/138/6456.html?view=joint&param=510 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[511](https://dblp.org/pid/138/6456.html?view=joint&param=511 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yugen Yi](https://dblp.org/pid/147/8410.html)

[\[j27\]](https://dblp.org/pid/138/6456.html#j27)

[512](https://dblp.org/pid/138/6456.html?view=joint&param=512 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[513](https://dblp.org/pid/138/6456.html?view=joint&param=513 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[514](https://dblp.org/pid/138/6456.html?view=joint&param=514 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chenyang Yu](https://dblp.org/pid/287/4163.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[515](https://dblp.org/pid/138/6456.html?view=joint&param=515 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Fisher Yu 0001](https://dblp.org/pid/117/6314.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[516](https://dblp.org/pid/138/6456.html?view=joint&param=516 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[517](https://dblp.org/pid/138/6456.html?view=joint&param=517 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[518](https://dblp.org/pid/138/6456.html?view=joint&param=518 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kaicheng Yu](https://dblp.org/pid/198/0861.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[519](https://dblp.org/pid/138/6456.html?view=joint&param=519 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ke Yu](https://dblp.org/pid/23/2089.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[520](https://dblp.org/pid/138/6456.html?view=joint&param=520 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[521](https://dblp.org/pid/138/6456.html?view=joint&param=521 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[522](https://dblp.org/pid/138/6456.html?view=joint&param=522 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaosheng Yu 0003](https://dblp.org/pid/99/8589-3.html)

[\[c25\]](https://dblp.org/pid/138/6456.html#c25)

[523](https://dblp.org/pid/138/6456.html?view=joint&param=523 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yang Yu 0010](https://dblp.org/pid/46/2181-10.html)

[\[c5\]](https://dblp.org/pid/138/6456.html#c5) [\[i7\]](https://dblp.org/pid/138/6456.html#i7)

[524](https://dblp.org/pid/138/6456.html?view=joint&param=524 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xing Yuan](https://dblp.org/pid/221/0150.html)

[\[j24\]](https://dblp.org/pid/138/6456.html#j24)

[525](https://dblp.org/pid/138/6456.html?view=joint&param=525 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Sangdoo Yun](https://dblp.org/pid/124/3009.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[526](https://dblp.org/pid/138/6456.html?view=joint&param=526 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[527](https://dblp.org/pid/138/6456.html?view=joint&param=527 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Belinda Zeng](https://dblp.org/pid/277/3956.html)

[\[c22\]](https://dblp.org/pid/138/6456.html#c22) [\[c21\]](https://dblp.org/pid/138/6456.html#c21) [\[i18\]](https://dblp.org/pid/138/6456.html#i18) [\[i17\]](https://dblp.org/pid/138/6456.html#i17)

[528](https://dblp.org/pid/138/6456.html?view=joint&param=528 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[529](https://dblp.org/pid/138/6456.html?view=joint&param=529 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xinlong Zhai](https://dblp.org/pid/402/0457.html)

[\[i32\]](https://dblp.org/pid/138/6456.html#i32)

[530](https://dblp.org/pid/138/6456.html?view=joint&param=530 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Baochang Zhang 0001](https://dblp.org/pid/80/3887-1.html)

[\[j8\]](https://dblp.org/pid/138/6456.html#j8) [\[i2\]](https://dblp.org/pid/138/6456.html#i2) [\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[531](https://dblp.org/pid/138/6456.html?view=joint&param=531 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bo Zhang](https://dblp.org/pid/36/2259.html)

[\[i5\]](https://dblp.org/pid/138/6456.html#i5)

[532](https://dblp.org/pid/138/6456.html?view=joint&param=532 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bo Zhang 0015](https://dblp.org/pid/36/2259-15.html)

[\[i1\]](https://dblp.org/pid/138/6456.html#i1)

[533](https://dblp.org/pid/138/6456.html?view=joint&param=533 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[534](https://dblp.org/pid/138/6456.html?view=joint&param=534 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chi Zhang 0021](https://dblp.org/pid/91/195-21.html)

[\[j4\]](https://dblp.org/pid/138/6456.html#j4)

[535](https://dblp.org/pid/138/6456.html?view=joint&param=535 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[536](https://dblp.org/pid/138/6456.html?view=joint&param=536 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[537](https://dblp.org/pid/138/6456.html?view=joint&param=537 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Guozhou Zhang](https://dblp.org/pid/230/2465.html)

[\[c4\]](https://dblp.org/pid/138/6456.html#c4)

[538](https://dblp.org/pid/138/6456.html?view=joint&param=538 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[539](https://dblp.org/pid/138/6456.html?view=joint&param=539 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Hongyi Zhang](https://dblp.org/pid/28/4536.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[540](https://dblp.org/pid/138/6456.html?view=joint&param=540 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiaming Zhang 0006](https://dblp.org/pid/81/10010-6.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[541](https://dblp.org/pid/138/6456.html?view=joint&param=541 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jian-Kang Zhang 0001](https://dblp.org/pid/94/1861-1.html)

aka: Jiankang Zhang 0001

[\[i1\]](https://dblp.org/pid/138/6456.html#i1)

[542](https://dblp.org/pid/138/6456.html?view=joint&param=542 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jianping Zhang](https://dblp.org/pid/03/2548.html)

[\[c1\]](https://dblp.org/pid/138/6456.html#c1)

[543](https://dblp.org/pid/138/6456.html?view=joint&param=543 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jie Zhang 0091](https://dblp.org/pid/84/6889-91.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[544](https://dblp.org/pid/138/6456.html?view=joint&param=544 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jin Zhang](https://dblp.org/pid/43/6657.html)

[\[j21\]](https://dblp.org/pid/138/6456.html#j21) [\[j20\]](https://dblp.org/pid/138/6456.html#j20) [\[j18\]](https://dblp.org/pid/138/6456.html#j18) [\[j10\]](https://dblp.org/pid/138/6456.html#j10)

[545](https://dblp.org/pid/138/6456.html?view=joint&param=545 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jing Zhang 0037](https://dblp.org/pid/05/3499-37.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[546](https://dblp.org/pid/138/6456.html?view=joint&param=546 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[547](https://dblp.org/pid/138/6456.html?view=joint&param=547 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[548](https://dblp.org/pid/138/6456.html?view=joint&param=548 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Kexin Zhang 0003](https://dblp.org/pid/119/0668-3.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[549](https://dblp.org/pid/138/6456.html?view=joint&param=549 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Li Zhang 0040](https://dblp.org/pid/89/5992-40.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[550](https://dblp.org/pid/138/6456.html?view=joint&param=550 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Luhao Zhang](https://dblp.org/pid/254/8164.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[551](https://dblp.org/pid/138/6456.html?view=joint&param=551 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Muhan Zhang](https://dblp.org/pid/157/5518.html)

[\[i34\]](https://dblp.org/pid/138/6456.html#i34)

[552](https://dblp.org/pid/138/6456.html?view=joint&param=552 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Peizhen Zhang](https://dblp.org/pid/115/9027.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[553](https://dblp.org/pid/138/6456.html?view=joint&param=553 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Pengyu Zhang](https://dblp.org/pid/33/4816.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[554](https://dblp.org/pid/138/6456.html?view=joint&param=554 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qing Zhang](https://dblp.org/pid/68/1429.html)

[\[c33\]](https://dblp.org/pid/138/6456.html#c33)

[555](https://dblp.org/pid/138/6456.html?view=joint&param=555 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qing Zhang 0004](https://dblp.org/pid/68/1429-4.html)

[\[j20\]](https://dblp.org/pid/138/6456.html#j20) [\[j18\]](https://dblp.org/pid/138/6456.html#j18) [\[j10\]](https://dblp.org/pid/138/6456.html#j10)

[556](https://dblp.org/pid/138/6456.html?view=joint&param=556 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ruixin Zhang](https://dblp.org/pid/132/6250.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[557](https://dblp.org/pid/138/6456.html?view=joint&param=557 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[558](https://dblp.org/pid/138/6456.html?view=joint&param=558 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wei Zhang 0021](https://dblp.org/pid/10/4661-21.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[559](https://dblp.org/pid/138/6456.html?view=joint&param=559 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenhua Zhang](https://dblp.org/pid/28/1877.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[560](https://dblp.org/pid/138/6456.html?view=joint&param=560 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[561](https://dblp.org/pid/138/6456.html?view=joint&param=561 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wenqing Zhang](https://dblp.org/pid/138/8580.html)

[\[j23\]](https://dblp.org/pid/138/6456.html#j23)

[562](https://dblp.org/pid/138/6456.html?view=joint&param=562 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[563](https://dblp.org/pid/138/6456.html?view=joint&param=563 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[564](https://dblp.org/pid/138/6456.html?view=joint&param=564 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xin Zhang 0008](https://dblp.org/pid/76/1584-8.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[565](https://dblp.org/pid/138/6456.html?view=joint&param=565 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[566](https://dblp.org/pid/138/6456.html?view=joint&param=566 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yanfu Zhang](https://dblp.org/pid/154/7698.html)

[\[c37\]](https://dblp.org/pid/138/6456.html#c37)

[567](https://dblp.org/pid/138/6456.html?view=joint&param=567 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yifan Zhang 0001](https://dblp.org/pid/57/4707-1.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[568](https://dblp.org/pid/138/6456.html?view=joint&param=568 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yisi Zhang](https://dblp.org/pid/318/0710.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[569](https://dblp.org/pid/138/6456.html?view=joint&param=569 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yu Zhang](https://dblp.org/pid/50/671.html)

[\[j4\]](https://dblp.org/pid/138/6456.html#j4)

[570](https://dblp.org/pid/138/6456.html?view=joint&param=570 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[571](https://dblp.org/pid/138/6456.html?view=joint&param=571 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[572](https://dblp.org/pid/138/6456.html?view=joint&param=572 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[573](https://dblp.org/pid/138/6456.html?view=joint&param=573 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c20\]](https://dblp.org/pid/138/6456.html#c20) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[574](https://dblp.org/pid/138/6456.html?view=joint&param=574 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bo Zhao 0037](https://dblp.org/pid/94/4810-37.html)

[\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[i25\]](https://dblp.org/pid/138/6456.html#i25)

[575](https://dblp.org/pid/138/6456.html?view=joint&param=575 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Haojie Zhao](https://dblp.org/pid/216/7590.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[576](https://dblp.org/pid/138/6456.html?view=joint&param=576 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[577](https://dblp.org/pid/138/6456.html?view=joint&param=577 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jing Zhao](https://dblp.org/pid/69/5882.html)

[\[j7\]](https://dblp.org/pid/138/6456.html#j7) [\[j5\]](https://dblp.org/pid/138/6456.html#j5)

[578](https://dblp.org/pid/138/6456.html?view=joint&param=578 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Juanping Zhao](https://dblp.org/pid/120/5177.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[579](https://dblp.org/pid/138/6456.html?view=joint&param=579 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Mengchen Zhao](https://dblp.org/pid/178/8719.html)

[\[i29\]](https://dblp.org/pid/138/6456.html#i29)

[580](https://dblp.org/pid/138/6456.html?view=joint&param=580 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Peilin Zhao](https://dblp.org/pid/84/8411.html)

[\[c15\]](https://dblp.org/pid/138/6456.html#c15) [\[c13\]](https://dblp.org/pid/138/6456.html#c13) [\[c10\]](https://dblp.org/pid/138/6456.html#c10) [\[i13\]](https://dblp.org/pid/138/6456.html#i13) [\[c5\]](https://dblp.org/pid/138/6456.html#c5) [\[i9\]](https://dblp.org/pid/138/6456.html#i9) [\[i7\]](https://dblp.org/pid/138/6456.html#i7) [\[i6\]](https://dblp.org/pid/138/6456.html#i6)

[581](https://dblp.org/pid/138/6456.html?view=joint&param=581 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[582](https://dblp.org/pid/138/6456.html?view=joint&param=582 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tianyu Zhao](https://dblp.org/pid/139/3492.html)

[\[c27\]](https://dblp.org/pid/138/6456.html#c27)

[583](https://dblp.org/pid/138/6456.html?view=joint&param=583 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiande Zhao](https://dblp.org/pid/76/5803.html)

[\[j23\]](https://dblp.org/pid/138/6456.html#j23)

[584](https://dblp.org/pid/138/6456.html?view=joint&param=584 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yanyun Zhao](https://dblp.org/pid/12/7547.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[585](https://dblp.org/pid/138/6456.html?view=joint&param=585 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zihao Zhao](https://dblp.org/pid/63/9613.html)

[\[i32\]](https://dblp.org/pid/138/6456.html#i32)

[586](https://dblp.org/pid/138/6456.html?view=joint&param=586 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zixiang Zhao](https://dblp.org/pid/65/5420.html)

[\[j25\]](https://dblp.org/pid/138/6456.html#j25) [\[i35\]](https://dblp.org/pid/138/6456.html#i35)

[587](https://dblp.org/pid/138/6456.html?view=joint&param=587 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[588](https://dblp.org/pid/138/6456.html?view=joint&param=588 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xiantong Zhen](https://dblp.org/pid/78/10651.html)

[\[j14\]](https://dblp.org/pid/138/6456.html#j14)

[589](https://dblp.org/pid/138/6456.html?view=joint&param=589 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[j26\]](https://dblp.org/pid/138/6456.html#j26) [\[j25\]](https://dblp.org/pid/138/6456.html#j25) [\[c40\]](https://dblp.org/pid/138/6456.html#c40) [\[i37\]](https://dblp.org/pid/138/6456.html#i37) [\[i35\]](https://dblp.org/pid/138/6456.html#i35) [\[i33\]](https://dblp.org/pid/138/6456.html#i33) [\[i30\]](https://dblp.org/pid/138/6456.html#i30) [\[j17\]](https://dblp.org/pid/138/6456.html#j17) [\[j15\]](https://dblp.org/pid/138/6456.html#j15) [\[j14\]](https://dblp.org/pid/138/6456.html#j14) [\[c37\]](https://dblp.org/pid/138/6456.html#c37) [\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c34\]](https://dblp.org/pid/138/6456.html#c34) [\[c32\]](https://dblp.org/pid/138/6456.html#c32) [\[i27\]](https://dblp.org/pid/138/6456.html#i27) [\[i26\]](https://dblp.org/pid/138/6456.html#i26) [\[i25\]](https://dblp.org/pid/138/6456.html#i25) [\[i22\]](https://dblp.org/pid/138/6456.html#i22) [\[i21\]](https://dblp.org/pid/138/6456.html#i21) [\[j11\]](https://dblp.org/pid/138/6456.html#j11) [\[c26\]](https://dblp.org/pid/138/6456.html#c26) [\[c25\]](https://dblp.org/pid/138/6456.html#c25) [\[i19\]](https://dblp.org/pid/138/6456.html#i19) [\[c20\]](https://dblp.org/pid/138/6456.html#c20) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c18\]](https://dblp.org/pid/138/6456.html#c18) [\[c16\]](https://dblp.org/pid/138/6456.html#c16) [\[i16\]](https://dblp.org/pid/138/6456.html#i16) [\[i15\]](https://dblp.org/pid/138/6456.html#i15) [\[i14\]](https://dblp.org/pid/138/6456.html#i14) [\[c12\]](https://dblp.org/pid/138/6456.html#c12) [\[i11\]](https://dblp.org/pid/138/6456.html#i11)

[590](https://dblp.org/pid/138/6456.html?view=joint&param=590 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[591](https://dblp.org/pid/138/6456.html?view=joint&param=591 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[592](https://dblp.org/pid/138/6456.html?view=joint&param=592 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shuangjia Zheng](https://dblp.org/pid/235/3743.html)

[\[c5\]](https://dblp.org/pid/138/6456.html#c5) [\[i7\]](https://dblp.org/pid/138/6456.html#i7)

[593](https://dblp.org/pid/138/6456.html?view=joint&param=593 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yaozong Zheng](https://dblp.org/pid/344/6907.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[594](https://dblp.org/pid/138/6456.html?view=joint&param=594 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[595](https://dblp.org/pid/138/6456.html?view=joint&param=595 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Cong Zhou](https://dblp.org/pid/44/3148.html)

[\[j22\]](https://dblp.org/pid/138/6456.html#j22)

[596](https://dblp.org/pid/138/6456.html?view=joint&param=596 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jinglin Zhou](https://dblp.org/pid/48/6808.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[597](https://dblp.org/pid/138/6456.html?view=joint&param=597 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Junbao Zhou](https://dblp.org/pid/340/7404.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[598](https://dblp.org/pid/138/6456.html?view=joint&param=598 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qiangqiang Zhou](https://dblp.org/pid/161/2504.html)

[\[c33\]](https://dblp.org/pid/138/6456.html#c33)

[599](https://dblp.org/pid/138/6456.html?view=joint&param=599 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Qimin Zhou](https://dblp.org/pid/220/1007.html)

[\[c42\]](https://dblp.org/pid/138/6456.html#c42)

[600](https://dblp.org/pid/138/6456.html?view=joint&param=600 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Tao Zhou](https://dblp.org/pid/98/4450.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20)

[601](https://dblp.org/pid/138/6456.html?view=joint&param=601 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Wengang Zhou 0001](https://dblp.org/pid/22/4544-1.html)

[\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[602](https://dblp.org/pid/138/6456.html?view=joint&param=602 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yong Zhou](https://dblp.org/pid/90/5836.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[603](https://dblp.org/pid/138/6456.html?view=joint&param=603 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Zikun Zhou](https://dblp.org/pid/271/8084.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[604](https://dblp.org/pid/138/6456.html?view=joint&param=604 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Guibo Zhu](https://dblp.org/pid/125/2113.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

[605](https://dblp.org/pid/138/6456.html?view=joint&param=605 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11)

[606](https://dblp.org/pid/138/6456.html?view=joint&param=606 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Pengfei Zhu 0001](https://dblp.org/pid/40/6172-1.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[607](https://dblp.org/pid/138/6456.html?view=joint&param=607 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Shengyin Zhu](https://dblp.org/pid/234/1707.html)

[\[c3\]](https://dblp.org/pid/138/6456.html#c3)

[608](https://dblp.org/pid/138/6456.html?view=joint&param=608 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xinliang Zhu](https://dblp.org/pid/160/9968.html)

[\[c30\]](https://dblp.org/pid/138/6456.html#c30) [\[i20\]](https://dblp.org/pid/138/6456.html#i20) [\[c8\]](https://dblp.org/pid/138/6456.html#c8) [\[c7\]](https://dblp.org/pid/138/6456.html#c7) [\[i8\]](https://dblp.org/pid/138/6456.html#i8)

[609](https://dblp.org/pid/138/6456.html?view=joint&param=609 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35) [\[c19\]](https://dblp.org/pid/138/6456.html#c19) [\[c11\]](https://dblp.org/pid/138/6456.html#c11) [\[c6\]](https://dblp.org/pid/138/6456.html#c6)

[610](https://dblp.org/pid/138/6456.html?view=joint&param=610 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c19\]](https://dblp.org/pid/138/6456.html#c19)

[611](https://dblp.org/pid/138/6456.html?view=joint&param=611 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/138/6456.html?view=group&param=1)

[Vladimir V. Zunin](https://dblp.org/pid/372/7918.html)

[\[c35\]](https://dblp.org/pid/138/6456.html#c35)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/138/6456.html#) [\[–\]](https://dblp.org/pid/138/6456.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/138/6456.html#) [\[–\]](https://dblp.org/pid/138/6456.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/138/6456.html#) [\[–\]](https://dblp.org/pid/138/6456.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/138/6456.html#) [\[–\]](https://dblp.org/pid/138/6456.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/138/6456.html#) [\[–\]](https://dblp.org/pid/138/6456.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)