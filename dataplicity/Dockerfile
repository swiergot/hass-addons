ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 2

RUN apk add --no-cache python2 nginx curl sudo shadow supervisor grep
RUN mkdir -p /etc/supervisor/conf.d /run/nginx

RUN cp /etc/supervisord.conf /etc/supervisord.conf.orig
COPY init_dataplicity /etc/cont-init.d/dataplicity
COPY init_nginx /etc/cont-init.d/nginx

RUN mkdir -p /etc/services.d/nginx /etc/services.d/supervisor
COPY run_nginx /etc/services.d/nginx/run
COPY run_supervisor /etc/services.d/supervisor/run
COPY nginx.conf /etc/nginx/default.conf.template
