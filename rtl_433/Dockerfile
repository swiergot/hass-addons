FROM bademux/rtl_433tomqtt

USER root

RUN apk add --no-cache jq

COPY run.sh /
RUN chmod a+x /run.sh

ENTRYPOINT [ "/usr/bin/env" ]
CMD [ "/run.sh" ]
