# syntax=docker/dockerfile:1

FROM gitlab-registry.cern.ch/cms-cloud/cmssw-docker/cc7-cms

COPY python /code/python
COPY install.sh /code/install.sh
COPY run.sh /code/run.sh

WORKDIR /code

RUN bash install.sh

WORKDIR /code

#EXPOSE 8070

ENTRYPOINT ["/bin/bash", "/code/run.sh"]

#CMD /bin/bash
