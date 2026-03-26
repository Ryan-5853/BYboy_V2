> 抓取来源：https://dblp.org/pid/230/6532.html

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

- [Fenglei Xue](https://dblp.org/pid/184/0264.html)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Fenglei+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Fenglei+Xu+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Fenglei+Xu+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Fenglei+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Fenglei+Xu+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Fenglei+Xu%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Fenglei+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F230%2F6532%3E+%7D+.%0A%0A%7D)

_showing all27 records_

2016202652017: 12018: 12020: 32021: 32021: 32021: 32022: 52022: 52022: 52023: 42023: 42024: 42025: 32025: 32026: 32026: 3

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

- ![](https://dblp.org/img/add-mark.12x12.png)Fuyuan Hu (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Fan Lyu (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Linyan Li (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Mingwu Ren (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Jing Lou (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Longtao Chen (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Kaile Du (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Huan Wang 0013 (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Bingwen Hu (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Huanqiang Zeng (4)

- _49 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (19)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-5454-157X (8)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Multim. Tools Appl. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IROS (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Knowl. Based Syst. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Multim. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Eng. Appl. Artif. Intell. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)BMVC (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Electr. Eng. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Mob. Networks Appl. (1)

- _7 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (17)
- ![](https://dblp.org/img/add-mark.12x12.png)open (9)
- ![](https://dblp.org/img/add-mark.12x12.png)unavailable (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j13\]
[Longtao Chen](https://dblp.org/pid/198/0702.html), [Jinjie Zheng](https://dblp.org/pid/292/0451.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fenglei Xu, [Fa Zhu](https://dblp.org/pid/61/10460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ajith Abraham](https://dblp.org/pid/a/AAbraham.html), [Huanqiang Zeng](https://dblp.org/pid/25/8798.html):

Enhancing Few-Shot marble slab surface defect detection: A diffusion framework with knowledge distillation and semantic guidance. [Eng. Appl. Artif. Intell.172](https://dblp.org/db/journals/eaai/eaai172.html#journals/eaai/ChenZXZAZ26): 114334 (2026)
- ![](https://dblp.org/img/n.png)

\[j12\]
[Longtao Chen](https://dblp.org/pid/198/0702.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guoxing Liao](https://dblp.org/pid/389/7910.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yifan Shi](https://dblp.org/pid/91/1278.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Lou](https://dblp.org/pid/54/9756.html), Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Huanqiang Zeng](https://dblp.org/pid/25/8798.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Hybrid-stage association with dynamicity adaptation and enhanced cues for multi-object tracking and segmentation. [Pattern Recognit.173](https://dblp.org/db/journals/pr/pr173.html#journals/pr/ChenLSLXZ26): 112803 (2026)
- ![](https://dblp.org/img/n.png)

\[i9\]
[Wentao Bian](https://dblp.org/pid/263/5406.html), Fenglei Xu:

Rethinking Multimodal Few-Shot 3D Point Cloud Segmentation: From Fused Refinement to Decoupled Arbitration. [CoRRabs/2601.01456](https://dblp.org/db/journals/corr/corr2601.html#journals/corr/abs-2601-01456) (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[c5\]
[Longtao Chen](https://dblp.org/pid/198/0702.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinjie Zheng](https://dblp.org/pid/292/0451.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Lou](https://dblp.org/pid/54/9756.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huanqiang Zeng](https://dblp.org/pid/25/8798.html)![](https://dblp.org/img/orcid-mark.12x12.png):

MSD: Mask-Guided and Semantic-Guided Diffusion-Based Framework for Stone Surface Defect Detection. [CVM (1)2025](https://dblp.org/db/conf/cvm/cvm2025-1.html#conf/cvm/ChenZXLZ25): 412-427
- ![](https://dblp.org/img/n.png)

\[c4\]
[Longtao Chen](https://dblp.org/pid/198/0702.html), [Guoxing Liao](https://dblp.org/pid/389/7910.html), [Jing Lou](https://dblp.org/pid/54/9756.html), Fenglei Xu, [Bingwen Hu](https://dblp.org/pid/215/8072.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lineng Chen](https://dblp.org/pid/230/6597.html), [Huanqiang Zeng](https://dblp.org/pid/25/8798.html):

Dynamicity Adaptation for Multi-object Tracking and Segmentation: Toward Improved Association Correction. [IROS2025](https://dblp.org/db/conf/iros/iros2025.html#conf/iros/ChenLLXHCZ25): 20556-20561
- ![](https://dblp.org/img/n.png)

\[i8\]
[Zhaoyi Meng](https://dblp.org/pid/186/2989.html), Fenglei Xu, [Wenxiang Zhao](https://dblp.org/pid/80/9614.html), [Wansen Wang](https://dblp.org/pid/00/6350-1.html), [Wenchao Huang](https://dblp.org/pid/47/7564-1.html), [Jie Cui](https://dblp.org/pid/55/3002-4.html), [Hong Zhong](https://dblp.org/pid/12/2179-1.html), [Yan Xiong](https://dblp.org/pid/70/880-1.html):

MalFlows: Context-aware Fusion of Heterogeneous Flow Semantics for Android Malware Detection. [CoRRabs/2508.03588](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-03588) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j11\]
[Feiyu Han](https://dblp.org/pid/28/6382.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Panlong Yang](https://dblp.org/pid/79/1482.html)![](https://dblp.org/img/orcid-mark.12x12.png), [You Zuo](https://dblp.org/pid/176/1220.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fei Shang](https://dblp.org/pid/11/7732.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang-Yang Li](https://dblp.org/pid/l/XiangYangLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

EarSpeech: Exploring In-Ear Occlusion Effect on Earphones for Data-efficient Airborne Speech Enhancement. [Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.8(3)](https://dblp.org/db/journals/imwut/imwut8.html#journals/imwut/HanYZSXL24): 104:1-104:30 (2024)
- ![](https://dblp.org/img/n.png)

\[j10\]
Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Haokai Zhao](https://dblp.org/pid/324/5640.html), [Yifei Wu](https://dblp.org/pid/95/9480.html), [Chongben Tao](https://dblp.org/pid/224/2350.html):

F-3DNet: Extracting inner order of point cloud for 3D object detection in autonomous driving. [Multim. Tools Appl.83(3)](https://dblp.org/db/journals/mta/mta83.html#journals/mta/XuZWT24): 8499-8516 (2024)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Lineng Chen](https://dblp.org/pid/230/6597.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Kong](https://dblp.org/pid/94/1836-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huan Wang](https://dblp.org/pid/70/6155-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wankou Yang](https://dblp.org/pid/99/3602.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Lou](https://dblp.org/pid/54/9756.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png):

HVP-Net: A Hybrid Voxel- and Point-Wise Network for Place Recognition. [IEEE Trans. Intell. Veh.9(1)](https://dblp.org/db/journals/tiv/tiv9.html#journals/tiv/ChenKWYLXR24): 395-406 (2024)
- ![](https://dblp.org/img/n.png)

\[j8\]
[Kaile Du](https://dblp.org/pid/315/8814.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fan Lyu](https://dblp.org/pid/227/4526.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linyan Li](https://dblp.org/pid/118/5692.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xuefeng Xi](https://dblp.org/pid/169/4586.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hanjing Cheng](https://dblp.org/pid/298/7062.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-Label Continual Learning Using Augmented Graph Convolutional Network. [IEEE Trans. Multim.26](https://dblp.org/db/journals/tmm/tmm26.html#journals/tmm/DuLLHFXXC24): 2978-2992 (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j7\]
[Chen Wang](https://dblp.org/pid/82/4206-41.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Shi](https://dblp.org/pid/88/9616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chongben Tao](https://dblp.org/pid/224/2350.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xinxin Tang](https://dblp.org/pid/189/3823.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liang Li](https://dblp.org/pid/14/1395-19.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuanyuan Zhou](https://dblp.org/pid/99/2747-7.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bokun Tian](https://dblp.org/pid/229/5904.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shunjun Wei](https://dblp.org/pid/42/9621.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaoling Zhang](https://dblp.org/pid/80/8951.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multitype Label Noise Modeling and Uncertainty-Weighted Label Correction for Concealed Object Detection. [IEEE Trans. Instrum. Meas.72](https://dblp.org/db/journals/tim/tim72.html#journals/tim/WangSTXTLZTWZ23): 1-12 (2023)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Hao Chen](https://dblp.org/pid/175/3324.html), [Linyan Li](https://dblp.org/pid/118/5692.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Zhenping Xia](https://dblp.org/pid/223/2415.html), Fenglei Xu:

Two-level Graph Network for Few-Shot Class-Incremental Learning. [CoRRabs/2303.13862](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-13862) (2023)
- ![](https://dblp.org/img/n.png)

\[i6\]
[Jiayao Tan](https://dblp.org/pid/206/9175.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Linyan Li](https://dblp.org/pid/118/5692.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Tingliang Feng](https://dblp.org/pid/235/0433.html), Fenglei Xu, [Rui Yao](https://dblp.org/pid/72/2221.html):

Dynamic V2X Autonomous Perception from Road-to-Vehicle Vision. [CoRRabs/2310.19113](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-19113) (2023)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Jian Zhang](https://dblp.org/pid/07/314.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Linyan Li](https://dblp.org/pid/118/5692.html), Fenglei Xu:

Constructing Sample-to-Class Graph for Few-Shot Class-Incremental Learning. [CoRRabs/2310.20268](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-20268) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j6\]
[Lineng Chen](https://dblp.org/pid/230/6597.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bingwen Hu](https://dblp.org/pid/215/8072.html), Fenglei Xu, [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png):

GR-LO: A specific lidar odometry system optimized with ground and road edges. [Comput. Electr. Eng.102](https://dblp.org/db/journals/cee/cee102.html#journals/cee/ChenHXR22): 108258 (2022)
- ![](https://dblp.org/img/n.png)

\[c3\]
[Kaile Du](https://dblp.org/pid/315/8814.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Linyan Li](https://dblp.org/pid/118/5692.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), Fenglei Xu, [Qiming Fu](https://dblp.org/pid/162/2675-1.html):

AGCN: Augmented Graph Convolutional Network for Lifelong Multi-Label Image Recognition. [ICME2022](https://dblp.org/db/conf/icmcs/icme2022.html#conf/icmcs/DuLHL0XF22): 1-6
- ![](https://dblp.org/img/n.png)

\[i4\]
[Kaile Du](https://dblp.org/pid/315/8814.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Linyan Li](https://dblp.org/pid/118/5692.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), Fenglei Xu, [Qiming Fu](https://dblp.org/pid/162/2675-1.html):

AGCN: Augmented Graph Convolutional Network for Lifelong Multi-label Image Recognition. [CoRRabs/2203.05534](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-05534) (2022)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Kaile Du](https://dblp.org/pid/315/8814.html), [Linyan Li](https://dblp.org/pid/118/5692.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Zhenping Xia](https://dblp.org/pid/223/2415.html), Fenglei Xu:

Class-Incremental Lifelong Learning in Multi-Label Classification. [CoRRabs/2207.07840](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-07840) (2022)
- ![](https://dblp.org/img/n.png)

\[i2\]
[Kaile Du](https://dblp.org/pid/315/8814.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Linyan Li](https://dblp.org/pid/118/5692.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), Fenglei Xu, [Xue-Feng Xi](https://dblp.org/pid/169/4586.html), [Hanjing Cheng](https://dblp.org/pid/298/7062.html):

Multi-Label Continual Learning using Augmented Graph Convolutional Network. [CoRRabs/2211.14763](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-14763) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[j5\]
[Chongben Tao](https://dblp.org/pid/224/2350.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haotian He](https://dblp.org/pid/302/9857.html), Fenglei Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jiecheng Cao](https://dblp.org/pid/302/9983.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Stereo priori RCNN based car detection on point level for autonomous driving. [Knowl. Based Syst.229](https://dblp.org/db/journals/kbs/kbs229.html#journals/kbs/TaoHXC21): 107346 (2021)
- ![](https://dblp.org/img/n.png)

\[c2\]
[Liuqing Zhao](https://dblp.org/pid/304/7669.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Kaizhu Huang](https://dblp.org/pid/99/3390.html), Fenglei Xu, [Linyan Li](https://dblp.org/pid/118/5692.html):

Each Attribute Matters: Contrastive Attention for Sentence-based Image Editing. [BMVC2021](https://dblp.org/db/conf/bmvc/bmvc2021.html#conf/bmvc/ZhaoLHHXL21): Article 339
- ![](https://dblp.org/img/n.png)

\[i1\]
[Liuqing Zhao](https://dblp.org/pid/304/7669.html), [Fan Lyu](https://dblp.org/pid/227/4526.html), [Fuyuan Hu](https://dblp.org/pid/135/9619.html), [Kaizhu Huang](https://dblp.org/pid/99/3390.html), Fenglei Xu, [Linyan Li](https://dblp.org/pid/118/5692.html):

Each Attribute Matters: Contrastive Attention for Sentence-based Image Editing. [CoRRabs/2110.11159](https://dblp.org/db/journals/corr/corr2110.html#journals/corr/abs-2110-11159) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j4\]
Fenglei Xu, [Huan Wang](https://dblp.org/pid/70/6155-13.html), [Bingwen Hu](https://dblp.org/pid/215/8072.html), [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Road Boundaries Detection based on Modified Occupancy Grid Map Using Millimeter-wave Radar. [Mob. Networks Appl.25(4)](https://dblp.org/db/journals/monet/monet25.html#journals/monet/XuWHR20): 1496-1503 (2020)
- ![](https://dblp.org/img/n.png)

\[j3\]
[Jing Lou](https://dblp.org/pid/54/9756.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huan Wang](https://dblp.org/pid/70/6155-13.html), [Longtao Chen](https://dblp.org/pid/198/0702.html), Fenglei Xu, [Qingyuan Xia](https://dblp.org/pid/198/1080.html), [Wei Zhu](https://dblp.org/pid/83/4805.html), [Mingwu Ren](https://dblp.org/pid/84/5438.html):

Exploiting color name space for salient object detection. [Multim. Tools Appl.79(15-16)](https://dblp.org/db/journals/mta/mta79.html#journals/mta/LouWCXXZR20): 10873-10897 (2020)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Longtao Chen](https://dblp.org/pid/198/0702.html), [Jing Lou](https://dblp.org/pid/54/9756.html), Fenglei Xu, [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Grid-based multi-object tracking with Siamese CNN based appearance edge and access region mechanism. [Multim. Tools Appl.79(47)](https://dblp.org/db/journals/mta/mta79.html#journals/mta/ChenLXR20): 35333-35351 (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2018
- ![](https://dblp.org/img/n.png)

\[j1\]
Fenglei Xu, [Bingwen Hu](https://dblp.org/pid/215/8072.html), [Lineng Chen](https://dblp.org/pid/230/6597.html), [Huan Wang](https://dblp.org/pid/70/6155-13.html), [Qingyuan Xia](https://dblp.org/pid/198/1080.html), [Paramjit S. Sehdev](https://dblp.org/pid/230/6572.html), [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png):

An illumination robust road detection method based on color names and geometric information. [Cogn. Syst. Res.52](https://dblp.org/db/journals/cogsr/cogsr52.html#journals/cogsr/XuHCWXSR18): 240-250 (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[c1\]
[Jing Lou](https://dblp.org/pid/54/9756.html), Fenglei Xu, [Qingyuan Xia](https://dblp.org/pid/198/1080.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Mingwu Ren](https://dblp.org/pid/84/5438.html):

Hierarchical Co-salient Object Detection via Color Names. [ACPR2017](https://dblp.org/db/conf/acpr/acpr2017.html#conf/acpr/LouXXYR17): 718-724
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/230/6532.html?view=joint&param=1 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Ajith Abraham](https://dblp.org/pid/a/AAbraham.html)

[\[j13\]](https://dblp.org/pid/230/6532.html#j13)

[2](https://dblp.org/pid/230/6532.html?view=joint&param=2 "show joint publications")

[Wentao Bian](https://dblp.org/pid/263/5406.html)

[\[i9\]](https://dblp.org/pid/230/6532.html#i9)

[3](https://dblp.org/pid/230/6532.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Jiecheng Cao](https://dblp.org/pid/302/9983.html)

[\[j5\]](https://dblp.org/pid/230/6532.html#j5)

[4](https://dblp.org/pid/230/6532.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Hao Chen](https://dblp.org/pid/175/3324.html)

[\[i7\]](https://dblp.org/pid/230/6532.html#i7)

[5](https://dblp.org/pid/230/6532.html?view=joint&param=5 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Lineng Chen](https://dblp.org/pid/230/6597.html)

[\[c4\]](https://dblp.org/pid/230/6532.html#c4) [\[j9\]](https://dblp.org/pid/230/6532.html#j9) [\[j6\]](https://dblp.org/pid/230/6532.html#j6) [\[j1\]](https://dblp.org/pid/230/6532.html#j1)

[6](https://dblp.org/pid/230/6532.html?view=joint&param=6 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Longtao Chen](https://dblp.org/pid/198/0702.html)

[\[j13\]](https://dblp.org/pid/230/6532.html#j13) [\[j12\]](https://dblp.org/pid/230/6532.html#j12) [\[c5\]](https://dblp.org/pid/230/6532.html#c5) [\[c4\]](https://dblp.org/pid/230/6532.html#c4) [\[j3\]](https://dblp.org/pid/230/6532.html#j3) [\[j2\]](https://dblp.org/pid/230/6532.html#j2)

[7](https://dblp.org/pid/230/6532.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Hanjing Cheng](https://dblp.org/pid/298/7062.html)

[\[j8\]](https://dblp.org/pid/230/6532.html#j8) [\[i2\]](https://dblp.org/pid/230/6532.html#i2)

[8](https://dblp.org/pid/230/6532.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Jie Cui 0004](https://dblp.org/pid/55/3002-4.html)

[\[i8\]](https://dblp.org/pid/230/6532.html#i8)

[9](https://dblp.org/pid/230/6532.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Kaile Du](https://dblp.org/pid/315/8814.html)

[\[j8\]](https://dblp.org/pid/230/6532.html#j8) [\[c3\]](https://dblp.org/pid/230/6532.html#c3) [\[i4\]](https://dblp.org/pid/230/6532.html#i4) [\[i3\]](https://dblp.org/pid/230/6532.html#i3) [\[i2\]](https://dblp.org/pid/230/6532.html#i2)

[10](https://dblp.org/pid/230/6532.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Tingliang Feng](https://dblp.org/pid/235/0433.html)

[\[i6\]](https://dblp.org/pid/230/6532.html#i6)

[11](https://dblp.org/pid/230/6532.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Wei Feng 0005](https://dblp.org/pid/17/1152-5.html)

[\[j8\]](https://dblp.org/pid/230/6532.html#j8) [\[c3\]](https://dblp.org/pid/230/6532.html#c3) [\[i4\]](https://dblp.org/pid/230/6532.html#i4) [\[i2\]](https://dblp.org/pid/230/6532.html#i2)

[12](https://dblp.org/pid/230/6532.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Qiming Fu 0001](https://dblp.org/pid/162/2675-1.html)

[\[c3\]](https://dblp.org/pid/230/6532.html#c3) [\[i4\]](https://dblp.org/pid/230/6532.html#i4)

[13](https://dblp.org/pid/230/6532.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Feiyu Han](https://dblp.org/pid/28/6382.html)

[\[j11\]](https://dblp.org/pid/230/6532.html#j11)

[14](https://dblp.org/pid/230/6532.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Haotian He](https://dblp.org/pid/302/9857.html)

[\[j5\]](https://dblp.org/pid/230/6532.html#j5)

[15](https://dblp.org/pid/230/6532.html?view=joint&param=15 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Bingwen Hu](https://dblp.org/pid/215/8072.html)

[\[c4\]](https://dblp.org/pid/230/6532.html#c4) [\[j6\]](https://dblp.org/pid/230/6532.html#j6) [\[j4\]](https://dblp.org/pid/230/6532.html#j4) [\[j1\]](https://dblp.org/pid/230/6532.html#j1)

[16](https://dblp.org/pid/230/6532.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Fuyuan Hu](https://dblp.org/pid/135/9619.html)

[\[j8\]](https://dblp.org/pid/230/6532.html#j8) [\[i7\]](https://dblp.org/pid/230/6532.html#i7) [\[i6\]](https://dblp.org/pid/230/6532.html#i6) [\[i5\]](https://dblp.org/pid/230/6532.html#i5) [\[c3\]](https://dblp.org/pid/230/6532.html#c3) [\[i4\]](https://dblp.org/pid/230/6532.html#i4) [\[i3\]](https://dblp.org/pid/230/6532.html#i3) [\[i2\]](https://dblp.org/pid/230/6532.html#i2) [\[c2\]](https://dblp.org/pid/230/6532.html#c2) [\[i1\]](https://dblp.org/pid/230/6532.html#i1)

[17](https://dblp.org/pid/230/6532.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Kaizhu Huang](https://dblp.org/pid/99/3390.html)

[\[c2\]](https://dblp.org/pid/230/6532.html#c2) [\[i1\]](https://dblp.org/pid/230/6532.html#i1)

[18](https://dblp.org/pid/230/6532.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Wenchao Huang 0001](https://dblp.org/pid/47/7564-1.html)

[\[i8\]](https://dblp.org/pid/230/6532.html#i8)

[19](https://dblp.org/pid/230/6532.html?view=joint&param=19 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Hui Kong 0001](https://dblp.org/pid/94/1836-1.html)

[\[j9\]](https://dblp.org/pid/230/6532.html#j9)

[20](https://dblp.org/pid/230/6532.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Liang Li 0019](https://dblp.org/pid/14/1395-19.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[21](https://dblp.org/pid/230/6532.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Linyan Li](https://dblp.org/pid/118/5692.html)

[\[j8\]](https://dblp.org/pid/230/6532.html#j8) [\[i7\]](https://dblp.org/pid/230/6532.html#i7) [\[i6\]](https://dblp.org/pid/230/6532.html#i6) [\[i5\]](https://dblp.org/pid/230/6532.html#i5) [\[c3\]](https://dblp.org/pid/230/6532.html#c3) [\[i4\]](https://dblp.org/pid/230/6532.html#i4) [\[i3\]](https://dblp.org/pid/230/6532.html#i3) [\[i2\]](https://dblp.org/pid/230/6532.html#i2) [\[c2\]](https://dblp.org/pid/230/6532.html#c2) [\[i1\]](https://dblp.org/pid/230/6532.html#i1)

[22](https://dblp.org/pid/230/6532.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Xiang-Yang Li 0001](https://dblp.org/pid/l/XiangYangLi.html)

[\[j11\]](https://dblp.org/pid/230/6532.html#j11)

[23](https://dblp.org/pid/230/6532.html?view=joint&param=23 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Guoxing Liao](https://dblp.org/pid/389/7910.html)

[\[j12\]](https://dblp.org/pid/230/6532.html#j12) [\[c4\]](https://dblp.org/pid/230/6532.html#c4)

[24](https://dblp.org/pid/230/6532.html?view=joint&param=24 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Jing Lou](https://dblp.org/pid/54/9756.html)

[\[j12\]](https://dblp.org/pid/230/6532.html#j12) [\[c5\]](https://dblp.org/pid/230/6532.html#c5) [\[c4\]](https://dblp.org/pid/230/6532.html#c4) [\[j9\]](https://dblp.org/pid/230/6532.html#j9) [\[j3\]](https://dblp.org/pid/230/6532.html#j3) [\[j2\]](https://dblp.org/pid/230/6532.html#j2) [\[c1\]](https://dblp.org/pid/230/6532.html#c1)

[25](https://dblp.org/pid/230/6532.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Fan Lyu](https://dblp.org/pid/227/4526.html)

[\[j8\]](https://dblp.org/pid/230/6532.html#j8) [\[i7\]](https://dblp.org/pid/230/6532.html#i7) [\[i6\]](https://dblp.org/pid/230/6532.html#i6) [\[i5\]](https://dblp.org/pid/230/6532.html#i5) [\[c3\]](https://dblp.org/pid/230/6532.html#c3) [\[i4\]](https://dblp.org/pid/230/6532.html#i4) [\[i3\]](https://dblp.org/pid/230/6532.html#i3) [\[i2\]](https://dblp.org/pid/230/6532.html#i2) [\[c2\]](https://dblp.org/pid/230/6532.html#c2) [\[i1\]](https://dblp.org/pid/230/6532.html#i1)

[26](https://dblp.org/pid/230/6532.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Zhaoyi Meng](https://dblp.org/pid/186/2989.html)

[\[i8\]](https://dblp.org/pid/230/6532.html#i8)

[27](https://dblp.org/pid/230/6532.html?view=joint&param=27 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Mingwu Ren](https://dblp.org/pid/84/5438.html)

[\[j9\]](https://dblp.org/pid/230/6532.html#j9) [\[j6\]](https://dblp.org/pid/230/6532.html#j6) [\[j4\]](https://dblp.org/pid/230/6532.html#j4) [\[j3\]](https://dblp.org/pid/230/6532.html#j3) [\[j2\]](https://dblp.org/pid/230/6532.html#j2) [\[j1\]](https://dblp.org/pid/230/6532.html#j1) [\[c1\]](https://dblp.org/pid/230/6532.html#c1)

[28](https://dblp.org/pid/230/6532.html?view=joint&param=28 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Paramjit S. Sehdev](https://dblp.org/pid/230/6572.html)

[\[j1\]](https://dblp.org/pid/230/6532.html#j1)

[29](https://dblp.org/pid/230/6532.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Fei Shang](https://dblp.org/pid/11/7732.html)

[\[j11\]](https://dblp.org/pid/230/6532.html#j11)

[30](https://dblp.org/pid/230/6532.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Jun Shi 0002](https://dblp.org/pid/88/9616.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[31](https://dblp.org/pid/230/6532.html?view=joint&param=31 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Yifan Shi](https://dblp.org/pid/91/1278.html)

[\[j12\]](https://dblp.org/pid/230/6532.html#j12)

[32](https://dblp.org/pid/230/6532.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Jiayao Tan](https://dblp.org/pid/206/9175.html)

[\[i6\]](https://dblp.org/pid/230/6532.html#i6)

[33](https://dblp.org/pid/230/6532.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Xinxin Tang](https://dblp.org/pid/189/3823.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[34](https://dblp.org/pid/230/6532.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Chongben Tao](https://dblp.org/pid/224/2350.html)

[\[j10\]](https://dblp.org/pid/230/6532.html#j10) [\[j7\]](https://dblp.org/pid/230/6532.html#j7) [\[j5\]](https://dblp.org/pid/230/6532.html#j5)

[35](https://dblp.org/pid/230/6532.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Bokun Tian](https://dblp.org/pid/229/5904.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[36](https://dblp.org/pid/230/6532.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Chen Wang 0041](https://dblp.org/pid/82/4206-41.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[37](https://dblp.org/pid/230/6532.html?view=joint&param=37 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Huan Wang 0013](https://dblp.org/pid/70/6155-13.html)

[\[j9\]](https://dblp.org/pid/230/6532.html#j9) [\[j4\]](https://dblp.org/pid/230/6532.html#j4) [\[j3\]](https://dblp.org/pid/230/6532.html#j3) [\[j1\]](https://dblp.org/pid/230/6532.html#j1)

[38](https://dblp.org/pid/230/6532.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Wansen Wang 0001](https://dblp.org/pid/00/6350-1.html)

[\[i8\]](https://dblp.org/pid/230/6532.html#i8)

[39](https://dblp.org/pid/230/6532.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Shunjun Wei](https://dblp.org/pid/42/9621.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[40](https://dblp.org/pid/230/6532.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Yifei Wu](https://dblp.org/pid/95/9480.html)

[\[j10\]](https://dblp.org/pid/230/6532.html#j10)

[41](https://dblp.org/pid/230/6532.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Xue-Feng Xi](https://dblp.org/pid/169/4586.html)

aka: Xuefeng Xi

[\[j8\]](https://dblp.org/pid/230/6532.html#j8) [\[i2\]](https://dblp.org/pid/230/6532.html#i2)

[42](https://dblp.org/pid/230/6532.html?view=joint&param=42 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Qingyuan Xia](https://dblp.org/pid/198/1080.html)

[\[j3\]](https://dblp.org/pid/230/6532.html#j3) [\[j1\]](https://dblp.org/pid/230/6532.html#j1) [\[c1\]](https://dblp.org/pid/230/6532.html#c1)

[43](https://dblp.org/pid/230/6532.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Zhenping Xia](https://dblp.org/pid/223/2415.html)

[\[i7\]](https://dblp.org/pid/230/6532.html#i7) [\[i3\]](https://dblp.org/pid/230/6532.html#i3)

[44](https://dblp.org/pid/230/6532.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Yan Xiong 0001](https://dblp.org/pid/70/880-1.html)

[\[i8\]](https://dblp.org/pid/230/6532.html#i8)

[45](https://dblp.org/pid/230/6532.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Panlong Yang](https://dblp.org/pid/79/1482.html)

[\[j11\]](https://dblp.org/pid/230/6532.html#j11)

[46](https://dblp.org/pid/230/6532.html?view=joint&param=46 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[j9\]](https://dblp.org/pid/230/6532.html#j9) [\[c1\]](https://dblp.org/pid/230/6532.html#c1)

[47](https://dblp.org/pid/230/6532.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Rui Yao](https://dblp.org/pid/72/2221.html)

[\[i6\]](https://dblp.org/pid/230/6532.html#i6)

[48](https://dblp.org/pid/230/6532.html?view=joint&param=48 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Huanqiang Zeng](https://dblp.org/pid/25/8798.html)

[\[j13\]](https://dblp.org/pid/230/6532.html#j13) [\[j12\]](https://dblp.org/pid/230/6532.html#j12) [\[c5\]](https://dblp.org/pid/230/6532.html#c5) [\[c4\]](https://dblp.org/pid/230/6532.html#c4)

[49](https://dblp.org/pid/230/6532.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Jian Zhang](https://dblp.org/pid/07/314.html)

[\[i5\]](https://dblp.org/pid/230/6532.html#i5)

[50](https://dblp.org/pid/230/6532.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Xiaoling Zhang 0002](https://dblp.org/pid/80/8951.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[51](https://dblp.org/pid/230/6532.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Haokai Zhao](https://dblp.org/pid/324/5640.html)

[\[j10\]](https://dblp.org/pid/230/6532.html#j10)

[52](https://dblp.org/pid/230/6532.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Liuqing Zhao](https://dblp.org/pid/304/7669.html)

[\[c2\]](https://dblp.org/pid/230/6532.html#c2) [\[i1\]](https://dblp.org/pid/230/6532.html#i1)

[53](https://dblp.org/pid/230/6532.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Wenxiang Zhao](https://dblp.org/pid/80/9614.html)

[\[i8\]](https://dblp.org/pid/230/6532.html#i8)

[54](https://dblp.org/pid/230/6532.html?view=joint&param=54 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Jinjie Zheng](https://dblp.org/pid/292/0451.html)

[\[j13\]](https://dblp.org/pid/230/6532.html#j13) [\[c5\]](https://dblp.org/pid/230/6532.html#c5)

[55](https://dblp.org/pid/230/6532.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Hong Zhong 0001](https://dblp.org/pid/12/2179-1.html)

[\[i8\]](https://dblp.org/pid/230/6532.html#i8)

[56](https://dblp.org/pid/230/6532.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[Yuanyuan Zhou 0007](https://dblp.org/pid/99/2747-7.html)

[\[j7\]](https://dblp.org/pid/230/6532.html#j7)

[57](https://dblp.org/pid/230/6532.html?view=joint&param=57 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Fa Zhu](https://dblp.org/pid/61/10460.html)

[\[j13\]](https://dblp.org/pid/230/6532.html#j13)

[58](https://dblp.org/pid/230/6532.html?view=joint&param=58 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=2)

[Wei Zhu](https://dblp.org/pid/83/4805.html)

[\[j3\]](https://dblp.org/pid/230/6532.html#j3)

[59](https://dblp.org/pid/230/6532.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/230/6532.html?view=group&param=1)

[You Zuo](https://dblp.org/pid/176/1220.html)

[\[j11\]](https://dblp.org/pid/230/6532.html#j11)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/230/6532.html#) [\[–\]](https://dblp.org/pid/230/6532.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/230/6532.html#) [\[–\]](https://dblp.org/pid/230/6532.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/230/6532.html#) [\[–\]](https://dblp.org/pid/230/6532.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/230/6532.html#) [\[–\]](https://dblp.org/pid/230/6532.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/230/6532.html#) [\[–\]](https://dblp.org/pid/230/6532.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)