tubemap = {"Aldgate" : ["Liverpool Street","Tower Hill"],
"Aldgate East" : ["Tower Hill","Liverpool Street"],
"Angel" : ["King's Cross St. Pancras","Old Street"],
"Baker Street" : ["Marylebone","Regent's Park","Edgware Road (C)","Great Portland Street","Bond Street"],
"Bank" : ["Liverpool Street","St. Paul's","London Bridge","Moorgate","Waterloo"],
"Barbican" : ["Farringdon","Moorgate"],
"Bayswater" : ["Paddington"],
"Blackfriars" : ["Mansion House","Temple"],
"Bond Street" : ["Marble Arch","Oxford Circus","Green Park","Baker Street"],
"Borough" : ["London Bridge"],
"Cannon Street" : ["Mansion House","Monument"],
"Chancery Lane" : ["Holborn","St. Paul's"],
"Charing Cross" : ["Embankment","Picadilly Circus","Leicester Square"],
"Covent Garden" : ["Holborn","Leicester Square"],
"Edgware Road (B)" : ["Marylebone","Paddington"],
"Edgware Road (C)" : ["Paddington","Baker Street"],
"Embankment" : ["Waterloo","Temple","Westminster","Charing Cross"],
"Euston" : ["King's Cross St. Pancras","Warren Street"],
"Euston Square" : ["Great Portland Street","King's Cross St. Pancras"],
"Farringdon" : ["King's Cross St. Pancras","Barbican"],
"Gloucester Road" : ["High Street Kensington","South Kensington"],
"Goodge Street" : ["Tottenham Court Road","Warren Street"],
"Great Portland Street" : ["Baker Street","Euston Square"],
"Green Park" : ["Westminster","Hyde Park Corner","Picadilly Circus","Oxford Circus","Victoria","Bond Street"],
"High Street Kensington" : ["Gloucester Road"],
"Holborn" : ["Tottenham Court Road","Russell Square","Chancery Lane","Covent Garden"],
"Hyde Park Corner" : ["Knightsbridge","Green Park"],
"King's Cross St. Pancras" : ["Russell Square","Euston Square","Farringdon","Angel","Euston"],
"Knightsbridge" : ["South Kensington","Hyde Park Corner"],
"Lambeth North" : ["Waterloo"],
"Lancaster Gate" : ["Marble Arch","Queensway"],
"Leicester Square" : ["Tottenham Court Road","Picadilly Circus","Charing Cross","Covent Garden"],
"Liverpool Street" : ["Moorgate","Bank","Aldgate","Aldgate East"],
"London Bridge" : ["Southwark","Bank","Borough"],
"Mansion House" : ["Blackfriars","Cannon Street"],
"Marble Arch" : ["Bond Street","Lancaster Gate"],
"Marylebone" : ["Baker Street","Edgware Road (B)"],
"Monument" : ["Tower Hill","Cannon Street"],
"Moorgate" : ["Old Street","Barbican","Liverpool Street","Bank"],
"Old Street" : ["Angel","Moorgate"],
"Oxford Circus" : ["Picadilly Circus","Regent's Park","Tottenham Court Road","Warren Street","Bond Street","Green Park"],
"Paddington" : ["Edgware Road (B)","Bayswater","Edgware Road (C)"],
"Picadilly Circus" : ["Charing Cross","Oxford Circus","Green Park","Leicester Square"],
"Pimlico" : ["Victoria"],
"Queensway" : ["Lancaster Gate"],
"Regent's Park" : ["Baker Street","Oxford Circus"],
"Russell Square" : ["Holborn","King's Cross St. Pancras"],
"Sloane Square" : ["South Kensington","Victoria"],
"South Kensington" : ["Gloucester Road","Sloane Square","Knightsbridge"],
"Southwark" : ["Waterloo","London Bridge"],
"St. James's Park" : ["Victoria","Westminster"],
"St. Paul's" : ["Bank","Chancery Lane"],
"Temple" : ["Blackfriars","Embankment"],
"Tottenham Court Road" : ["Holborn","Oxford Circus","Goodge Street","Leicester Square"],
"Tower Hill" : ["Aldgate","Monument","Aldgate East"],
"Victoria" : ["Sloane Square","St. James's Park","Green Park","Pimlico"],
"Warren Street" : ["Euston","Goodge Street","Oxford Circus"],
"Waterloo" : ["Westminster","Embankment","Lambeth North","Southwark","Bank"],
"Westminster" : ["Embankment","St. James's Park","Green Park","Waterloo"]}


def find_shortest_path(graph, start, end, shortestLength=-1, path=[]):
  path = path + [start]
  if start == end:
    return path
  if not graph.has_key(start):
    return None
  shortest = None
  for node in graph[start]:
    if node not in path:
      if shortestLength==-1 or len(path)<(shortestLength-1):
        newpath = find_shortest_path(graph, node, end, shortestLength, path)
        if newpath:
          if not shortest or len(newpath) < len(shortest):
            shortest = newpath
            shortestLength = len(newpath)  
  return shortest