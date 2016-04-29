import heapq

def perform_compute(args,plist,tlist):
    freq_list = {}
    # calculate N frequent customers
    if args.has_key("n_value"):
        for k in tlist:
            if k["cid"] not in freq_list:
                freq_list[k["cid"]] = 1
            else:
                freq_list[k["cid"]] += 1
        freq_heap = []
        for k in freq_list:
            heapq.heappush(freq_heap,(k,freq_list[k]))
        s = ""
        cnt = 0
        smallest = None
        for k,v in sorted(freq_heap,key=lambda x:x[1], reverse=True):
            if cnt < int(args['n_value']):
                if smallest != k[1]:
                    cnt += 1
                s += str(k)+" "+str(v)+","
                smallest = v
            else:
                if v == smallest:
                    s += str(k)+" "+str(v)+","
                else:
                    break
        print s
        # calculate N highest transactions
        cost_list = []
        tid = 0
        for k in tlist:
            t = ()
            price = 0
            for bid in k["bid"]:
                for p in plist:
                    if p["bookid"] == bid:
                        price += int(p["price"])
            cost_list.append((k["cid"],price))
        cost_heap = []
        for k in cost_list:
            heapq.heappush(cost_heap,(k[0],k[1]))
        s = ""
        cnt = 0
        smallest = None
        for k in sorted(cost_heap,key=lambda x:x[1],reverse=True):
            if cnt < int(args['n_value']):
                if smallest != k[1]:
                    cnt += 1
                s += k[0]+" "+str(k[1])+","
                smallest = k[1]
            else:
                if k[1] == smallest:
                    s += k[0]+" "+str(k[1])+","
                else:
                    break
        print s
        # calculate N highest selling books
        book_list = {}
        for k in tlist:
            for bid in k["bid"]:
                if bid not in book_list:
                    book_list[bid] = 1
                else:
                    book_list[bid] += 1
        sell_heap = []
        for k in book_list:
            heapq.heappush(sell_heap,(k,book_list[k]))

        cnt = 0
        s = ""
        smallest = None
        for k in sorted(sell_heap,key=lambda x:x[1],reverse=True):
            if cnt < int(args['n_value']):
                if smallest != k[1]:
                    cnt += 1
                s += k[0]+" "+str(k[1])+","
                smallest = k[1]
            else:
                if k[1] == smallest:
                    s += k[0]+" "+str(k[1])+","
                else:
                    break
        print s
        # calcualte N least selling books
        book_list = {}
        for k in plist:
            if k["bookid"] not in book_list:
                book_list[k["bookid"]] = 0
        for k in tlist:
            for bid in k["bid"]:
                book_list[bid] += 1
        sell_heap = []
        for k in book_list:
            heapq.heappush(sell_heap,(k,book_list[k]))

        s = ""
        cnt = 0
        smallest = None
        for k in sorted(sell_heap,key=lambda x:x[1]):
            if cnt < int(args['n_value']):
                if smallest != k[1]:
                    cnt += 1
                s += k[0]+" "+str(k[1])+","
                smallest = k[1]
            else:
                if k[1] == smallest:
                    s += k[0]+" "+str(k[1])+","
                else:
                    break

        print s
    if args.has_key("d_value"): 
        d_val = int(args["d_value"])
        c_val = args["c_value"]
        cust_list = {}
        for k in tlist:
            if k["cid"] not in cust_list:
                cust_list[k["cid"]] = 0
            for bid in k["bid"]:
                for p in plist:
                    if bid == p["bookid"]:
                        cust_list[k["cid"]] += int(p["price"])
        if c_val in cust_list and cust_list[c_val] > d_val:
            print 1
        else:
            print 0


            



